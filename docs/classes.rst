Classes
#######


OpenRGB
*******

This is the main class you'll be interfacing with to control OpenRGB,
implementing the SDK server protocol.

Ideally, the only functions that a relevant for general use are `client_name()`
and `devices()` as with `devices()` you gain access to Objects representing 
most of what you would have interest in doing.

.. autoclass:: openrgb.OpenRGB
    :members:
    :undoc-members:


ORGBDevice
**********

`ORGBDevice` is the class which is used to understand the device response
from the SDK Server. You shouldn't need to every directly instantiate this class,
but reading it's attributes is needed to get information on a device.

.. autoclass:: openrgb.ORGBDevice
    :undoc-members:

ORGBMode
********

.. autoclass:: openrgb.ORGBMode
    :members:
    :undoc-members:


ORGBZone
********

.. autoclass:: openrgb.ORGBZone
    :members:
    :undoc-members:


ORGBLED
*******

.. autoclass:: openrgb.ORGBLED
    :members:
    :undoc-members:

ORGBDeviceTypes
***************

This is an enumerator for all the possible device types.

.. autoclass:: openrgb.ORGBDeviceType
    :members: 
    :undoc-members:
