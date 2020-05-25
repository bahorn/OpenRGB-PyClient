Classes
#######


OpenRGB
*******

This is the main class you'll be interfacing with to control OpenRGB

.. autoclass:: openrgb.OpenRGB
    :members:
    :undoc-members:


ORGBDevice
**********

`ORGBDevice` is the class which is used to understand the device response
from the SDK Server. You shouldn't need to every directly instantiate this class,
but reading it's attributes is needed to get information on a device.

.. autoclass:: openrgb.ORGBDevice
    :members: __init__
    :undoc-members:

ORGBDeviceTypes
***************

This is an enumerator for all the possible device types.

.. autoclass:: openrgb.ORGBDeviceType
    :members: 
    :undoc-members:
