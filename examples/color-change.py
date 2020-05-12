import time
import sys,os

sys.path.append(os.path.realpath('.'))
from openrgb import OpenRGB


seq = [0x5bcefa00, 0xff1493, 0xffffff, 0xff1493, 0x5bcefa00]

client = OpenRGB('localhost', 1337)
count = client.controller_count()
devices = {}
for i in range(count):
    devices[i] = client.controller_data(device_id=i)
    led_count = len(devices[i].leds)
    cmap = []
    for j in range(led_count):
        idx = int(len(seq)*(j/led_count))
        cmap.append(seq[idx])
    client.update_leds(cmap, device_id=i)

