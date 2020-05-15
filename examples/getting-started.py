# Adding the library to our PYTHONPATH
import sys,os
sys.path.append(os.path.realpath('.'))

from openrgb import OpenRGB

client = OpenRGB('localhost', 1337)

devices = {}
for i in range(client.controller_count()):
    devices[i] = client.controller_data(device_id=i)

print(devices)

for _, device in devices.items():
    print('{} has {} LED(s)'.format(device.name, len(device.leds)))
