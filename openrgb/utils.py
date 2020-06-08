import struct

# we represent the color as a tuple of RGB values, so we need to
# correctly pack into a 32bit int for the library.


def pack_color(color):
    return struct.pack('BBBx', color[0], color[1], color[2])


def prepend_length(data):
    return struct.pack('I', len(data)) + data
