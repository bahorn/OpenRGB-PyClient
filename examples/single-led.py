import time
import sys,os

sys.path.append(os.path.realpath('.'))
from openrgb import OpenRGB


client = OpenRGB('localhost', 1337)
count = client.controller_count()
devices = {}
for i in range(count):
    devices[i] = client.controller_data(device_id=i)
    led_count = len(devices[i].leds)
    client.update_single_led(0, (255, 0, 0), device_id=i)

