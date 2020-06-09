import socket
import struct


from .consts import HeaderFmt, HeaderSize, MagicBytes


class Network:
    def __init__(self, host, port):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((host, port))

    # protocol helpers
    def _make_header(self, dev_idx, pkt_type, pkt_size):
        return struct.pack(
            HeaderFmt,
            MagicBytes,
            dev_idx,
            pkt_type,
            pkt_size
        )

    def send_message(self, cmd, data=b'', device_id=0):
        header = self._make_header(
            device_id,
            cmd.value,
            len(data)
        )
        packet = header + data
        self.s.send(packet)

    def recv_message(self):
        # validate the header:
        magic, dev_idx, pkt_type, pkt_size = struct.unpack(
            HeaderFmt, self.s.recv(HeaderSize)
        )
        if magic != MagicBytes:
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
