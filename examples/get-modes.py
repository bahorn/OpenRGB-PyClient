import time
import sys,os

sys.path.append(os.path.realpath('.'))
from openrgb import OpenRGB

client = OpenRGB('localhost', 1337)
count = client.controller_count()
for i in range(count):
    device = client.controller_data(device_id=i)
    print('{} - {}'.format(device.name, device.type))
    for mode in device.modes:
        print('* {} -  {}'.format(mode['value'], mode['name']))
    print()
