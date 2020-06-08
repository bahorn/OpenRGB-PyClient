import struct

from .ORGBDevice import ORGBDevice, ORGBMode
from .consts import ORGBPkt
from .utils import pack_color
from .Network import Network


class OpenRGB:
    def __init__(self, host, port, client_string='python client'):
        self.con = Network(host, port)
        self.client_name(client_string)

    # Network stuff
    def client_name(self, name=None):
        if name is not None:
            self.client_string = name
        self.con.send_message(
            ORGBPkt.SET_CLIENT_NAME,
            bytes(self.client_string, 'ascii')
        )

    def controller_count(self):
        self.con.send_message(ORGBPkt.REQUEST_CONTROLLER_COUNT)
        msg = self.con.recv_message()
        _, count = msg
        count = struct.unpack('I', count)[0]
        return count

    def controller_data(self, device_id=0):
        self.con.send_message(
            ORGBPkt.REQUEST_CONTROLLER_DATA,
            device_id=device_id
        )
        msg = self.con.recv_message()
        return ORGBDevice(msg[1], device_id, owner=self)

    # Generator for getting devices
    def devices(self):
        device_count = self.controller_count()
        for device_id in range(device_count):
            yield self.controller_data(device_id)

    # RGB controllers

    def resize_zone(self, zone_id, new_size, device_id=0):
        # this is device specific, but does just require sending a zone_id
        # and a new_size. Both are (signed) ints.
        # None of my devices (@bahorn as of 2020-05-13) support resizing, so I
        # can't really test this.

        # however, this *should* work:
        msg = struct.pack('ii', zone_id, new_size)
        self.con.send_message(
           ORGBPkt.RGBCONTROLLER_RESIZEZONE,
           data=msg,
           device_id=device_id,
        )

        # if you have a device that supports it and are willing to test, PRs
        # are accepted!
        pass

    def set_custom_mode(self, device_id=0):
        # this just calls the function SetCustomMode() in the RGB controller,
        # which in most cases just sets the active mode to 0.
        self.con.send_message(
            ORGBPkt.RGBCONTROLLER_SETCUSTOMMODE,
            device_id=device_id
        )

    def set_update_mode(self, mode, device_id=0, speed=None, direction=None,
                        color_mode=None):
        data = None
        # this requires getting the device info
        if type(mode) is ORGBMode:
            data = mode
        else:
            data = self.controller_data(device_id).modes[mode]

        data.speed = speed or data.speed
        data.direction = direction or data.direction
        data.color_mode = color_mode or data.color_mode

        self.con.send_message(
            ORGBPkt.RGBCONTROLLER_UPDATEMODE,
            data=OpenRGB._add_length(bytes(data)),
            device_id=device_id
        )

    # LED Control
    def update_leds(self, color_collection, device_id=0):
        c_buf = struct.pack('H', len(color_collection))
        for i in color_collection:
            c_buf += pack_color(i)
        # Add an accurate length.
        self.con.send_message(
            ORGBPkt.RGBCONTROLLER_UPDATELEDS,
            data=OpenRGB._add_length(c_buf),
            device_id=device_id
        )

    def update_zone_leds(self, zone_id, color_collection, device_id=0):
        # Essentially the same as update_leds, but with a zone_id.
        c_buf = struct.pack('IH', zone_id, len(color_collection))
        for i in color_collection:
            c_buf += pack_color(i)

        self.con.send_message(
            ORGBPkt.RGBCONTROLLER_UPDATEZONELEDS,
            data=OpenRGB._add_length(c_buf),
            device_id=device_id
        )

    def update_single_led(self, led, color, device_id=0):
        msg = struct.pack('i', led) + pack_color(color)
        self.con.send_message(
            ORGBPkt.RGBCONTROLLER_UPDATESINGLELED,
            data=msg,
            device_id=device_id
        )

    @staticmethod
    def _add_length(data):
        return struct.pack('I', len(data)) + data
