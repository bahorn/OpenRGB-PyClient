import time
import sys,os

sys.path.append(os.path.realpath('.'))
from openrgb import OpenRGB

client = OpenRGB('localhost', 1337)

for device in client.devices():
    print('{} - {}'.format(device.name, device.type))
    for mode in device.modes:
        print('* {} -  {}'.format(mode['value'], mode['name']))
    print()

print(client.controller_data(4).modes)
client.set_update_mode(1, 4, speed=4)
