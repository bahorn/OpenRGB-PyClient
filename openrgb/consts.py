from enum import Enum
import struct

class ORGBPkt(Enum):
    REQUEST_CONTROLLER_COUNT      = 0
    REQUEST_CONTROLLER_DATA       = 1
    SET_CLIENT_NAME               = 50
    RGBCONTROLLER_RESIZEZONE      = 1000
    RGBCONTROLLER_UPDATELEDS      = 1050
    RGBCONTROLLER_UPDATEZONELEDS  = 1051
    RGBCONTROLLER_UPDATESINGLELED = 1052
    RGBCONTROLLER_SETCUSTOMMODE   = 1100
    RGBCONTROLLER_UPDATEMODE      = 1101

class ORGBDeviceType(Enum):
    MOTHERBOARD = 0
    DRAM = 1
    GPU = 2
    COOLER = 3
    LEDSTRIP = 4
    KEYBOARD = 5
    MOUSE = 6
    MOUSEMAT = 7
    HEADSET = 8
    UNKNOWN = 9

class ORGBZoneType(Enum):
    SINGLE = 0
    LINEAR = 1
    MATRIX = 2

MagicBytes = bytes('ORGB', 'ascii')
HeaderFmt = '4sIII'
HeaderSize = struct.calcsize(HeaderFmt)
