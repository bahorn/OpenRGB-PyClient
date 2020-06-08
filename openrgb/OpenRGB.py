import socket
import struct

from .ORGBDevice import ORGBDevice
from .consts import ORGBPkt
from .utils import pack_color
from .binreader import Blob


class OpenRGB:
    # define these constants.
    magic = bytes('ORGB', 'ascii')
    header_fmt = '4sIII'
    header_size = struct.calcsize(header_fmt)

    def __init__(self, host, port, client_string='python client'):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((host, port))
        self.client_name(client_string)

    # Network stuff
    def client_name(self, name=None):
        if name is not None:
            self.client_string = name
        self._send_message(
            ORGBPkt.SET_CLIENT_NAME,
            bytes(self.client_string, 'ascii')
        )

    def controller_count(self):
        self._send_message(ORGBPkt.REQUEST_CONTROLLER_COUNT)
        msg = self._recv_message()
        _, count = msg
        count = struct.unpack('I', count)[0]
        return count

    def controller_data(self, device_id=0):
        self._send_message(
            ORGBPkt.REQUEST_CONTROLLER_DATA,
            device_id=device_id
        )
        msg = self._recv_message()
        return ORGBDevice(msg[1], device_id)

    # Generator for getting devices
    def devices(self):
        device_count = self.controller_count()
        for device_id in range(device_count):
            yield self.controller_data(device_id)

    # RGB controllers

    # not implemented
    def resize_zone(self, zone_id, new_size, device_id=0):
        # this is device specific, but does just require sending a zone_id
        # and a new_size. Both are (signed) ints.
        # None of my devices (@bahorn as of 2020-05-13) support resizing, so I
        # can't really test this.

        # however, this *should* work:
        # msg = struct.pack('ii', zone_id, new_size)
        # self._send_message(
        #   ORGBPkt.RGBCONTROLLER_RESIZEZONE,
        #   data=msg,
        #   device_id=device_id,
        # )

        # if you have a device that supports it and are willing to test, PRs
        # are accepted!
        pass

    def set_custom_mode(self, device_id=0):
        # this just calls the function SetCustomMode() in the RGB controller,
        # which in most cases just sets the active mode to 0.
        self._send_message(
            ORGBPkt.RGBCONTROLLER_SETCUSTOMMODE,
            device_id=device_id
        )

    def set_update_mode(self, mode, device_id=0, speed=None, direction=None,
                        color_mode=None):
        # this requires getting the device info
        data = self.controller_data(device_id)
        cur_mode = data.modes[mode]
        msg = Blob()
        msg.int(mode)
        msg.string(cur_mode['name'])
        msg.int(cur_mode['value'])
        msg.uint(cur_mode['flags'])
        msg.uint(cur_mode['speed_min'])
        msg.uint(cur_mode['speed_max'])
        msg.uint(cur_mode['colors_min'])
        msg.uint(cur_mode['colors_max'])

        # settings
        msg.uint(speed or cur_mode['speed'])
        msg.uint(direction or cur_mode['direction'])
        msg.uint(color_mode or cur_mode['color_mode'])

        msg.ushort(len(cur_mode['colors']))
        for color in cur_mode['colors']:
            msg.color(color)

        c_buf = struct.pack('I', len(msg.data))
        c_buf += msg.data

        self._send_message(
            ORGBPkt.RGBCONTROLLER_UPDATEMODE,
            data=c_buf,
            device_id=device_id
        )
        pass

    # LED Control
    def update_leds(self, color_collection, device_id=0):
        c_buf = struct.pack('H', len(color_collection))
        for i in color_collection:
            c_buf += pack_color(i)
        # Add an accurate length.
        real = struct.pack('I', len(c_buf)) + c_buf
        self._send_message(
            ORGBPkt.RGBCONTROLLER_UPDATELEDS,
            data=real,
            device_id=device_id
        )

    def update_zone_leds(self, zone_id, color_collection, device_id=0):
        # Essentially the same as update_leds, but with a zone_id.
        c_buf = struct.pack('IH', zone_id, len(color_collection))
        for i in color_collection:
            c_buf += pack_color(i)

        real = struct.pack('I', len(c_buf)) + c_buf
        self._send_message(
            ORGBPkt.RGBCONTROLLER_UPDATEZONELEDS,
            data=real,
            device_id=device_id
        )

    def update_single_led(self, led, color, device_id=0):
        msg = struct.pack('i', led) + pack_color(color)
        self._send_message(
            ORGBPkt.RGBCONTROLLER_UPDATESINGLELED,
            data=msg,
            device_id=device_id
        )

    # protocol helpers
    def _make_header(self, dev_idx, pkt_type, pkt_size):
        return struct.pack(
            self.header_fmt,
            self.magic,
            dev_idx,
            pkt_type,
            pkt_size
        )

    def _send_message(self, cmd, data=b'', device_id=0):
        header = self._make_header(
            device_id,
            cmd.value,
            len(data)
        )
        packet = header + data
        self.s.send(packet)

    def _recv_message(self):
        # validate the header:
        magic, dev_idx, pkt_type, pkt_size = struct.unpack(
            self.header_fmt, self.s.recv(self.header_size)
        )
        if magic != self.magic:
            raise Exception('Invalid packet received')

        # try to read it all in.
        buf = b''
        if pkt_size > 0:
            left = pkt_size
            while left > 0:
                buf += self.s.recv(left)
                left = pkt_size - len(buf)

        return (
            (dev_idx, pkt_type),
            buf
        )
