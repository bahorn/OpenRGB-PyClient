import sys, os
sys.path.append(os.path.realpath('.'))

from openrgb import OpenRGB

client = OpenRGB('localhost', 6742)

devices = list(client.devices())

print(devices[0].modes[1].active())
