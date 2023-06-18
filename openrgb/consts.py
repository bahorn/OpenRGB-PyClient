from enum import Enum
import struct

class ORGBPkt(Enum):
    REQUEST_CONTROLLER_COUNT      = 0
    REQUEST_CONTROLLER_DATA       = 1
    REQUEST_PROTOCOL_VERSION      = 40
    SET_CLIENT_NAME               = 50
    DEVICE_LIST_UPDATE            = 100
    REQUEST_PROFILE_LIST          = 150
    REQUEST_SAVE_PROFILE          = 151
    REQUEST_LOAD_PROFILE          = 152
    REQUEST_DELETE_PROFILE        = 153
    RGBCONTROLLER_RESIZEZONE      = 1000
    RGBCONTROLLER_UPDATELEDS      = 1050
    RGBCONTROLLER_UPDATEZONELEDS  = 1051
    RGBCONTROLLER_UPDATESINGLELED = 1052
    RGBCONTROLLER_SETCUSTOMMODE   = 1100
    RGBCONTROLLER_UPDATEMODE      = 1101
    RGBCONTROLLER_SAVEMODE        = 1102

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
    HEADSET_STAND = 9
    GAMEPAD = 10
    LIGHT = 11
    SPEAKER = 12
    VIRTUAL = 13
    UNKNOWN = 14

class ORGBZoneType(Enum):
    SINGLE = 0
    LINEAR = 1
    MATRIX = 2

class ORGBProtoVersion(Enum):
    V0 = 0
    V1 = 1
    V2 = 2
    V3 = 3

MagicBytes = bytes('ORGB', 'utf-8')
HeaderFmt = '4sIII'
HeaderSize = struct.calcsize(HeaderFmt)
