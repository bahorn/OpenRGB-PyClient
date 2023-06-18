import sys, os
sys.path.append(os.path.realpath('.'))

from openrgb import OpenRGB

client = OpenRGB('localhost', 6742)

for device in client.devices():
    print('{} - {}'.format(device.name, device.type))
    possible = {
        'Direct': None,
        'Static': None,
    }
    for mode in device.modes:
        print('* {} -  {}'.format(mode['value'], mode['name']))
        if mode.name in possible:
            possible[mode.name] = mode

    preference = [
        'Static', 'Direct'
    ]
    for modetype in preference:
        if possible[modetype] is not None:
            possible[modetype].active()
            break

    device.set((0,0,0))
