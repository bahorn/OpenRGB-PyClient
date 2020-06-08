from .consts import ORGBDeviceType, ORGBZoneType
from .binreader import Blob


class ORGBDevice:
    """
    ORGB is used to read device responses from the OpenRGB SDK server

    :attribute type: Device Type. This 
    :attribute name: Name of the device
    :attribute desc: Description of the device
    :attribute version: Device Version
    :attribute serial: Device Serial
    :attribute location: Device location
    :attribute active_mode: Devices Active Mode
    :attribute modes: List of modes
    :attribute zones: List of zones
    :attribute leds: List of LEDs
    :attribute colors: List of colors

    """

    def __init__(self, data, device_id=0):
        # hacky stupid way of doing this.
        self.id = device_id
        blob = Blob(data)
        length = blob.uint()
        if length != len(data):
            raise Exception('Length incorrect?')

        self.type = ORGBDeviceType(blob.uint())
        self.name = blob.string()
        self.desc = blob.string()
        self.version = blob.string()
        self.serial = blob.string()

        self.location = blob.string()

        n_modes = blob.ushort()
        self.active_mode = blob.uint()

        self.modes = []
        for mode_idx in range(n_modes):
            modename = blob.string()
            value = blob.int()
            flags = blob.uint()
            speed_min = blob.uint()
            speed_max = blob.uint()
            colors_min = blob.uint()
            colors_max = blob.uint()
            speed = blob.uint()
            direction = blob.uint()
            color_mode = blob.uint()

            color_len = blob.ushort()
            colors = []
            for color_index in range(color_len):
                colors.append(blob.color())

            new_mode = {
                'id': mode_idx,
                'name': modename,
                'value': value,
                'flags': flags,
                'speed_min': speed_min,
                'speed_max': speed_max,
                'colors_min':colors_min,
                'colors_max': colors_max,
                'speed': speed,
                'direction': direction,
                'color_mode': color_mode,
                'colors': colors
            }
            self.modes.append(new_mode)


        n_zones = blob.ushort()
        self.zones = []
        for zone_idx in range(n_zones):
            zonename = blob.string()
            zonetype = ORGBZoneType(blob.int())
            leds_min = blob.uint()
            leds_max = blob.uint()
            leds_count = blob.uint()

            matrix_size = blob.ushort()
            blob.skip(matrix_size)

            new_zone = {
                'name': zonename,
                'type': zonetype,
                'leds_min': leds_min,
                'leds_max': leds_max,
                'leds_count': leds_count,

            }
            self.zones.append(new_zone)

        n_leds = blob.ushort()
        self.leds = []
        for led_idx in range(n_leds):
            led_name = blob.string()
            led_value = blob.color()

            new_led = {
                'name': led_name,
                'value': led_value
            }
            self.leds.append(new_led)

        n_colors = blob.ushort()
        self.colors = []
        for color_idx in range(n_colors):
            self.colors.append(blob.color())

    def __repr__(self):
        return '{} - {}'.format(self.name, self.type)

