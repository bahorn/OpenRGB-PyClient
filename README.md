# OpenRGB Python Client

[OpenRGB](https://gitlab.com/CalcProgrammer1/OpenRGB) 
dropped it's server protocol into master yesterday, so
I wrote this hacky little client library to use it.

## Protocol

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
