import time
from openrgb import OpenRGB


if __name__ == '__main__':
    client = OpenRGB('localhost', 1337)
    count = client.controller_count()
    devices = {}
    for i in range(count):
        devices[i] = client.controller_data(device_id=i)
        led_count = len(devices[i].leds)
        client.update_leds([0x00]*led_count, device_id=i)


    val = 0
    while True:
        val += 1
        i = 0
        for i in range(count):
            cur = devices[i]
            led_count = len(cur.leds)
            client.update_leds([0x2f*val]*led_count, device_id=i)

        time.sleep(1)
