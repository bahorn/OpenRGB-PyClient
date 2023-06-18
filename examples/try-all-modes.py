import time

import sys, os
sys.path.append(os.path.realpath('.'))

from openrgb import OpenRGB

client = OpenRGB('localhost', 6742)

for device in client.devices():
    for mode in device.modes:
        mode.active()
        time.sleep(0.1)
