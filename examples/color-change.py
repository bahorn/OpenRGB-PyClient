import time
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

client = OpenRGB('localhost', 1337)

for device in client.devices():
    led_count = len(device.leds)
    cmap = []
    for j in range(led_count):
        idx = int(len(seq)*(j/led_count))
        cmap.append(seq[idx])
    client.update_leds(cmap, device_id=device.id)
