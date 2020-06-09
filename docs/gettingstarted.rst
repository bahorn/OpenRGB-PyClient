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

    devices = client.devices()

And if we print devices, we get (subject to change due to your hardware)::
    
    {0: ASUS Aura Motherboard - ORGBDeviceType.MOTHERBOARD, 1: Corsair Vengeance Pro RGB - ORGBDeviceType.DRAM, 2: Corsair Vengeance Pro RGB - ORGBDeviceType.DRAM, 3: AMD Wraith Prism - ORGBDeviceType.COOLER, 4: SteelSeries Rival 110 - ORGBDeviceType.MOUSE}


Now, we can then start to get data like how many LEDs each device has::

    for device in devices:
        print('{} has {} LEDs'.format(device.name, len(device.leds)))

Giving us something like::

    ASUS Aura Motherboard has 8 LEDs
    Corsair Vengeance Pro RGB has 10 LEDs
    Corsair Vengeance Pro RGB has 10 LEDs
    AMD Wraith Prism has 3 LEDs
    SteelSeries Rival 110 has 1 LEDs


Now, if we wanted to make all devices red, we can do something like this::
    
    for device in devices:
        device.set((255, 0, 0))


If we wanted to make the first led on each device blue::

    for device in devices:
        device.leds[0].set((0, 0, 255))

And if we wanted to make everything that supports a rainbow mode, rainbow::

    for device in devices:
        for mode in device.modes:
            if mode.name == 'Rainbow': mode.active()
