import struct

from .ORGBDevice import ORGBDevice, ORGBMode
from .consts import ORGBPkt, ORGBProtoVersion
from .utils import pack_color, prepend_length
from .Network import Network


class OpenRGB:
    def __init__(self, host, port=6742, client_string='python client'):
        self.con = Network(host, port)
        self.client_name(client_string)

    # Network stuff
    def client_name(self, name=None):
        """
        This sets the client name in the ORGB SDK server to the name provided.

        This lets you identify which programs are currently connected.
        """
        if name is not None:
            self.client_string = name
        self.con.send_message(
            ORGBPkt.SET_CLIENT_NAME,
            bytes(self.client_string, 'utf-8')
        )

    def controller_count(self):
        """
        This returns the count of active controllers in OpenRGB.
        """
        self.con.send_message(ORGBPkt.REQUEST_CONTROLLER_COUNT)
        msg = self.con.recv_message()
        _, count = msg
        count = struct.unpack('I', count)[0]
        return count

    def controller_data(self, device_id=0):
        """
        This returns an `ORGBDevice` constructed from the response given by
        the SDK Server, with device_id being the identifier for each device.
        """
        self.con.send_message(
            ORGBPkt.REQUEST_CONTROLLER_DATA,
            device_id=device_id
        )
        msg = self.con.recv_message()
        return ORGBDevice(msg[1], device_id, owner=self)

    # Generator for getting devices
    def devices(self):
        """
        This provides a generator for iterating through all the devices OpenRGB
        can find.

        This is the recommended interface for finding devices.
        """
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
        """
        This calls `RGBController::SetCustomMode`, which in most cases
        sets the active mode to 0.
        """
        self.con.send_message(
            ORGBPkt.RGBCONTROLLER_SETCUSTOMMODE,
            device_id=device_id
        )

    def set_update_mode(self, mode, device_id=0, speed=None, direction=None,
                        color_mode=None):
        """
        This is the protocol level way of setting the mode.

        `mode` can either be the mode id, or an `ORGBMode` object, though in the
        second case it's preferable to use it directly to set the active mode.
        """
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
            data=prepend_length(bytes(data)),
            device_id=device_id
        )

    # LED Control
    
    def update_leds(self, color_collection, device_id=0):
        """
        This is the protocol level function for setting multiple LEDs at once.
        """
        c_buf = struct.pack('H', len(color_collection))
        for i in color_collection:
            c_buf += pack_color(i)
        # Add an accurate length.
        self.con.send_message(
            ORGBPkt.RGBCONTROLLER_UPDATELEDS,
            data=prepend_length(c_buf),
            device_id=device_id
        )

    def update_zone_leds(self, zone_id, color_collection, device_id=0):
        """
        This is the protocol level function for setting a zones LEDs.
        
        Essentially the same as update_leds, but with a zone_id.
        """
        c_buf = struct.pack('IH', zone_id, len(color_collection))
        for i in color_collection:
            c_buf += pack_color(i)

        self.con.send_message(
            ORGBPkt.RGBCONTROLLER_UPDATEZONELEDS,
            data=prepend_length(c_buf),
            device_id=device_id
        )

    def update_single_led(self, led, color, device_id=0):
        """
        This is the protocol level function for setting a single LED.
        """
        msg = struct.pack('i', led) + pack_color(color)
        self.con.send_message(
            ORGBPkt.RGBCONTROLLER_UPDATESINGLELED,
            data=msg,
            device_id=device_id
        )
    
    # Profile Control
    
    def profiles(self):
        """
        This returns a list of profiles.
        """
        self.con.send_message(ORGBPkt.REQUEST_PROFILE_LIST)
        msg = self.con.recv_message()
        _, data = msg
        length, profiles_count = struct.unpack('IH', data[:6])
        profiles = []
        pos = 6
        for i in range(profiles_count):
            str_length, = struct.unpack('H', data[pos:pos+2])
            profile_name = data[pos+2:pos+2+str_length].decode().strip('\x00')
            profiles.append(profile_name)
            pos += 2+str_length
        
        return profiles
    
    def load_profile(self, profile_name):
        """
        This loads a profile given the name.
        
        Note that loading fails when the OpenRGB GUI is open and a different profile is selected in the dropdown.
        """
        self.con.send_message(
            ORGBPkt.REQUEST_LOAD_PROFILE,
            data=bytes(profile_name, 'utf-8')
        )
    
    def save_profile(self, profile_name):
        """
        This saves a profile given the name.
        """
        self.con.send_message(
            ORGBPkt.REQUEST_SAVE_PROFILE,
            data=bytes(profile_name, 'utf-8')
        )
    
    def delete_profile(self, profile_name):
        """
        This deletes a profile given the name.
        """
        self.con.send_message(
            ORGBPkt.REQUEST_DELETE_PROFILE,
            data=bytes(profile_name, 'utf-8')
        )

    def get_version(self):
        """
        This returns the protocol version.
        """
        self.con.send_message(
            ORGBPkt.REQUEST_PROTOCOL_VERSION
        )
        msg = self.con.recv_message()
        return ORGBProtoVersion(struct.unpack('I', msg[1])[0])
