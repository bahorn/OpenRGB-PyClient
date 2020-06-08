import time
import sys,os

sys.path.append(os.path.realpath('.'))
from openrgb import OpenRGB


seq = [
    (214, 2, 112),
    (0, 56, 168),
    (155, 79, 150),
    (0, 56, 168),
    (214, 2, 112)
]

client = OpenRGB('localhost', 1337)

for device in client.devices():
    for mode in device.modes:
        if mode.name == 'Static':
            mode.active()
            break
    for zone in device.zones:
        zone.set(seq, interpolate=True)
