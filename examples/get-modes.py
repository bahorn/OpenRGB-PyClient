import time
import sys,os

sys.path.append(os.path.realpath('.'))
from openrgb import OpenRGB

client = OpenRGB('localhost', 6742)

for device in client.devices():
    print('{} - {}'.format(device.name, device.type))
    for mode in device.modes:
        print('* {} -  {}'.format(mode['value'], mode['name']))
    print()
