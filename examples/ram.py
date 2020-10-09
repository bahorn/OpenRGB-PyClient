import time
import sys
import os
import random

sys.path.append(os.path.realpath('.'))
from openrgb import OpenRGB

client = OpenRGB('localhost', 6742)

# find and clear
devices = []
for device in client.devices():
    if device.name == "Corsair Vengeance Pro RGB":
        for mode in device.modes:
            if mode.name == "Direct":
                mode.active()
        device.set((0, 0, 0))
        devices.append(device)

# Truth Table
pattern = {
    (True, True, True): False,
    (True, True, False): True,
    (True, False, True): True,
    (True, False, False): False,
    (False, True, True): True,
    (False, True, False): True,
    (False, False, True): True,
    (False, False, False): False
}


# initial state
def inc_state(state=None):
    new_state = [False for i in range(10)]
    if state is not None:
        for i in range(10):
            h = i+1
            if h >= 10:
                h = 0
            new_state[i] = pattern[(state[i-1], state[i], state[h])]

    return new_state


state = inc_state([random.random() >= 0.75 for i in range(10)])
states = [state, state, state]

brightness = 10
while True:
    p = 0
    for device in [devices[2], devices[0], devices[1]]:
        leds = [
            (brightness*i, brightness*i, brightness*i) for i in states[p]]
        device.set(leds)
        p += 1
    time.sleep(1.0)
    states.append(inc_state(states[-1]))
    states = states[1:]
    if states[0] == states[1] == states[2]:
        states[-1] = inc_state([random.random() >= 0.75 for i in range(10)])
