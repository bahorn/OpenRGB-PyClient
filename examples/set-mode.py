import time
import sys,os
import random

sys.path.append(os.path.realpath('.'))
from openrgb import OpenRGB

client = OpenRGB('localhost', 6742)

for device in client.devices():
    print('{} - {}'.format(device.name, device.type))
    device.set((
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255)
    ))

    possible = {
        'Static': None,
        'Pulsate': None,
        'Rainbow': None,
        'Rainbow Mood': None,
        'Rainbow Wave': None
    }
    for mode in device.modes:
        print('* {} -  {}'.format(mode['value'], mode['name']))
        if mode.name in possible:
            possible[mode.name] = mode

    preference = [
        'Rainbow Wave', 'Rainbow Mood', 'Rainbow', 'Pulsate', 'Static'
    ]
    for modetype in preference:
        if possible[modetype] is not None:
            possible[modetype].active()
            break
