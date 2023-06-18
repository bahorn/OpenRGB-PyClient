import time
import psutil

import sys, os
sys.path.append(os.path.realpath('.'))

from openrgb import OpenRGB

client = OpenRGB('localhost', 6742)

# find and clear
for device in client.devices():
    device.set((0, 0, 0))

while True:
    load = psutil.cpu_percent()
    for device in client.devices():
        led_count = len(device.leds)
        leds_active = int((load/100)*led_count)
        device.set(
            [(255, 0, 255)]*leds_active +
            [(0, 0, 0)]*(led_count - leds_active)
        )
    time.sleep(0.1)
