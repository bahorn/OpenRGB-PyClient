import sys, os
sys.path.append(os.path.realpath('.'))

from openrgb import OpenRGB

seq = [
    (91, 206, 250),
    (245, 169, 184),
    (255, 255, 255),
    (245, 169, 184),
    (91, 206, 250)
]

client = OpenRGB('localhost', 6742)

for device in client.devices():
    for mode in device.modes:
        if mode.name == 'Static':
            mode.active()
            break
    device.set(seq, interpolate=True)
