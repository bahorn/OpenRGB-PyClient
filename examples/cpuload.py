import time
import psutil
import sys,os

sys.path.append(os.path.realpath('.'))
from openrgb import OpenRGB


client = OpenRGB('localhost', 1337)
count = client.controller_count()
devices = {}


# find and clear
for i in range(count):
    devices[i] = client.controller_data(device_id=i)
    led_count = len(devices[i].leds)
    client.update_leds([0x00]*led_count, device_id=i)


while True:
    load = psutil.cpu_percent()
    for did, device in devices.items():
        led_count = len(device.leds)
        leds_active = int((load/100)*led_count)
        print(leds_active)
        client.update_leds(
            [0xff00ff]*leds_active + [0x00]*(led_count - leds_active),
            device_id=did
        )
    time.sleep(0.1)
