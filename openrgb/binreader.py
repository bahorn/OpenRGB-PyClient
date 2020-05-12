import struct

# Allows extracting of values from binary blobs
class Blob:
 
    def __init__(self, data, idx=0):
        self.data = data
        self.idx = idx
    def _unpack(self, fmt):
        size = struct.calcsize(fmt)
        res = struct.unpack(fmt, self.data[self.idx: self.idx + size])
        self.idx += size
        return res

    def ushort(self):
        return self._unpack('H')[0]
    def uint(self):
        return self._unpack('I')[0]
    def int(self):
        return self._unpack('i')[0]
    def color(self):
        return self._unpack('cccc')
    def string(self):
        total_len = self.ushort()
        return self._unpack(
            '{}s'.format(total_len)
        )[0].decode('ascii')
    def skip(self, count):
        self._unpack('x'*count)
