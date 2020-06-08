import time
import sys,os
import random

sys.path.append(os.path.realpath('.'))
from openrgb import OpenRGB

client = OpenRGB('localhost', 1337)

for device in client.devices():
    print('{} - {}'.format(device.name, device.type))
    for mode in device.modes:
        print('* {} -  {}'.format(mode['value'], mode['name']))
        if mode['name'] == 'Static':
            mode.active()
            device.set((
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255)
            ))
        if mode['name'] == 'Rainbow':
            mode.active()
            break
