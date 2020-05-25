Protocol
########

Header
******

Each message (from either the client or the server) has a header of the format::

    char[4] magic
    unsigned int device_id
    unsigned int packet_type
    unsigned int packet_size

The `magic` just contains the characters 'ORGB', and is used to identify if the
packet is real.

`device_id` is used to specify which device you want to control or obtain info
from. For messages that are general and don't refer to a specific device, this
is set to 0.

`packet_type` refers to what the message is about. You can see the full list in
[#NetworkProtocol]_

`packet_size` is the total amount of bytes of the binary payload. Some commands
don't send anything, so this gets set to 0.


Packet Types
************

REQUEST_CONTROLLER_COUNT
========================

You send this to the count of devices, which you can then enumerate with
`REQUEST_CONTROLLER_DATA`.

To use this, set `packet_size` and `device_id` to 0 as this has no request
payload.

You get a response back (with a header) containing an unsigned integer
representing the total device count.

REQUEST_CONTROLLER_DATA
=======================

You use this to get a copy of the structure describing a device.

So, you need to set `device_id` to something in the range you got from the
controller count.

The response is a fairly large object that needs a bit of processing, so it's
recommended you read my implementation [#ORGBDevice]_


.. [#NetworkProtocol] https://gitlab.com/CalcProgrammer1/OpenRGB/-/blob/master/NetworkProtocol.h
.. [#ORGBDevice] https://github.com/bahorn/openrgb/ORGBDevice.py
