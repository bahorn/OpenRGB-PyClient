# OpenRGB Python Client

[OpenRGB](https://gitlab.com/CalcProgrammer1/OpenRGB) 
dropped it's server protocol into master yesterday, so
I wrote this hacky little client library to use it.

## Usage

**note** This is subject to change as the library is still early in development.
I do intend to make cleaner abstractions at some point, but for now it's fairly
low level. The examples folder should contain enough code to get started, but
you'll end up having to read the source if you want to do anything more complex.

First, you need to import the library:

```python3
from openrgb import OpenRGB
```

Then you can connect to your SDK server instance by using instantiating the
OpenRGB object with the details needed to connect to your SDK server instance.

```python3
client = OpenRGB('localhost', 1337)
```

Now we can start doing interesting things! Lets go through and read all the
device details:

```python3
# Find out how many devices there are, and collect all their data.
devices = {}
for i in range(client.controller_count()):
    devices[i] = client.controller_data(device_id=i)
```

And if we print devices, we get (subject to change due to your hardware):

```
{0: ASUS Aura Motherboard - ORGBDeviceType.MOTHERBOARD, 1: Corsair Vengeance Pro RGB - ORGBDeviceType.DRAM, 2: Corsair Vengeance Pro RGB - ORGBDeviceType.DRAM, 3: AMD Wraith Prism - ORGBDeviceType.COOLER, 4: SteelSeries Rival 110 - ORGBDeviceType.MOUSE}
```

Now, we can then start to get data like how many LEDs each device has:

```
for _, device in devices.items():
    print('{} has {} LED(s)'.format(device.name, len(device.leds)))
```

```
ASUS Aura Motherboard has 8 LEDs
Corsair Vengeance Pro RGB has 10 LEDs
Corsair Vengeance Pro RGB has 10 LEDs
AMD Wraith Prism has 3 LEDs
SteelSeries Rival 110 has 1 LEDs
```

## Protocol

In case anyone else needs a reference:

### Header

Each message (from either the client or the server) has a header of the format:

```
char[4] magic
unsigned int device_id
unsigned int packet_type
unsigned int packet_size
```

The `magic` just contains the characters 'ORGB', and is used to identify if the
packet is real.

`device_id` is used to specify which device you want to control or obtain info
from. For messages that are general and don't refer to a specific device, this
is set to 0.

`packet_type` refers to what the message is about. You can see the full list
[here](https://gitlab.com/CalcProgrammer1/OpenRGB/-/blob/master/NetworkProtocol.h)

`packet_size` is the total amount of bytes of the binary payload. Some commands
don't send anything, so this gets set to 0.


### Packet Types

#### REQUEST_CONTROLLER_COUNT

You send this to the count of devices, which you can then enumerate with
`REQUEST_CONTROLLER_DATA`.

To use this, set `packet_size` and `device_id` to 0 as this has no request
payload.

You get a response back (with a header) containing an unsigned integer
representing the total device count.

#### REQUEST_CONTROLLER_DATA

You use this to get a copy of the structure describing a device.

So, you need to set `device_id` to something in the range you got from the
controller count.

The response is a fairly large object that needs a bit of processing, so it's
recommended you read my implementation in [openrgb/ORGBDevice.py](openrgb/ORGBDevice.py).
