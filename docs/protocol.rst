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

SET_CLIENT_NAME
===============

This is how you set the name that appears in the SDK server pane of the GUI.

It takes a string which is your name, with the names length set in the packet
header. (`packet_size`)

RGBCONTROLLER_RESIZEZONE
========================

Very few devices support this.

RGBCONTROLLER_UPDATELEDS
========================

You provide a list of 32 bit colors, starting with the total count and it will
change the leds starting from led 0, all the way to led n.

You need to send one color for every LED.

RGBCONTROLLER_UPDATEZONELEDS
============================

This works in a similar way to UPDATELEDS, but includes an extra zoneid at the
start of the packet.

This is so you can say, apply it only to one collection of LEDS in a device.

RGBCONTROLLER_UPDATESINGLELED
=============================

This takes an signed integer representing the LED id, along with the color
represented as a 32 bit int (RGBx).

RGBCONTROLLER_SETCUSTOMMODE
===========================

This just sets the active mode to 0 for most devices, which is generally the
static color mode.

Takes no option, just needs a device as defined in the packet header.

RGBCONTROLLER_UPDATEMODE
========================

This lets you send over an entirely new mode object.

The main way to use this is to take an existing one, and send that, with just
things like speed, direction or color mode changed. Can do some hacky things
with this.

.. [#NetworkProtocol] https://gitlab.com/CalcProgrammer1/OpenRGB/-/blob/master/NetworkProtocol.h
.. [#ORGBDevice] https://github.com/bahorn/openrgb/ORGBDevice.py
