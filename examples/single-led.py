import time
import sys,os

sys.path.append(os.path.realpath('.'))
from openrgb import OpenRGB

client = OpenRGB('localhost', 6742)
for device in client.devices():
    print(device)
    device.leds[0].set((255, 0, 255))
