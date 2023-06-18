import sys, os
sys.path.append(os.path.realpath('.'))

from openrgb import OpenRGB

client = OpenRGB('localhost', 6742)

devices = list(client.devices())

print(devices)

for device in devices:
    print('{} has {} LED(s)'.format(device.name, len(device.leds)))
