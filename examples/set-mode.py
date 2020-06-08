import time
import sys,os

sys.path.append(os.path.realpath('.'))
from openrgb import OpenRGB

client = OpenRGB('localhost', 1337)

for device in client.devices():
    print('{} - {}'.format(device.name, device.type))
    for mode in device.modes:
        print('* {} -  {}'.format(mode['value'], mode['name']))
        if mode['name'] == 'Rainbow':
            # happy pride :)
            client.set_update_mode(mode['id'], device.id)
    print()


