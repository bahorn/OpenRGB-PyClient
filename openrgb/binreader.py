import struct


# Allows writing / extracting of values from binary blobs
class Blob:
    def __init__(self, data=None, idx=0):
        self.data = data or b''
        self.idx = idx

    def _unpack(self, fmt):
        size = struct.calcsize(fmt)
        res = struct.unpack(fmt, self.data[self.idx: self.idx + size])
        self.idx += size
        return res

    def _pack(self, fmt, data):

        if type(data) in (tuple, list):
            res = struct.pack(fmt, *data)
        else:
            res = struct.pack(fmt, data)

        self.data += res
        return res

    # An abstraction to avoid having to create a new class to handle writing.
    def _packer(self, fmt, data=None):
        if data is None:
            return self._unpack(fmt)
        return self._pack(fmt, data)

    def ushort(self, value=None):

        return self._packer('H', value)[0]

    def uint(self, value=None):

        return self._packer('I', value)[0]

    def int(self, value=None):

        return self._packer('i', value)[0]

    def color(self, value=None):

        return self._packer('cccx', value)

    def string(self, value=None):
        if value is not None:
            total_len = len(value)+1
            self.ushort(total_len)
            packed = self._pack(
                '{}s'.format(total_len), bytes(value, 'ascii')+b'\x00'
            )
            return packed
        else:
            total_len = self.ushort()
            unpacked = self._unpack(
                '{}s'.format(total_len)
            )[0].decode('ascii')
            if unpacked[-1] == '\x00':
                return unpacked[:-1]
            return unpacked

    def skip(self, count):
        self._packer('x'*count)
