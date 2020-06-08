import sys
import os

sys.path.append(os.path.realpath('.'))


from openrgb import OpenRGB


client = OpenRGB('localhost', 1337)
devices = [d for d in client.devices()]
print(devices[4].modes[1].active())
