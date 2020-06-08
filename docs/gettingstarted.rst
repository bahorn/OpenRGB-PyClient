Getting Started
###############

You can find examples on how to use the library in the `examples/ <https://github.com/bahorn/OpenRGB-PyClient/tree/master/examples>`_
directory in the projects repository

Walkthrough 
************

If you haven't already, install the library by `pip`::
    
    pip install OpenRGB-PyClient

First, you need to import the library::

    from openrgb import OpenRGB

Then you can connect to your SDK server instance by using instantiating the
OpenRGB object with the details needed to connect to your SDK server instance.::

    client = OpenRGB('localhost', 1337)

Now we can start doing interesting things! Lets go through and read all the
device details::

    # Find out how many devices there are, and collect all their data.
    devices = {}
    for i in range(client.controller_count()):
        devices[i] = client.controller_data(device_id=i)

And if we print devices, we get (subject to change due to your hardware)::
    
    {0: ASUS Aura Motherboard - ORGBDeviceType.MOTHERBOARD, 1: Corsair Vengeance Pro RGB - ORGBDeviceType.DRAM, 2: Corsair Vengeance Pro RGB - ORGBDeviceType.DRAM, 3: AMD Wraith Prism - ORGBDeviceType.COOLER, 4: SteelSeries Rival 110 - ORGBDeviceType.MOUSE}


Now, we can then start to get data like how many LEDs each device has::

    for _, device in devices.items():
        print('{} has {} LED(s)'.format(device.name, len(device.leds)))

Giving us something like::

    ASUS Aura Motherboard has 8 LEDs
    Corsair Vengeance Pro RGB has 10 LEDs
    Corsair Vengeance Pro RGB has 10 LEDs
    AMD Wraith Prism has 3 LEDs
    SteelSeries Rival 110 has 1 LEDs
