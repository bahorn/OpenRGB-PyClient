# OpenRGB Python Client

[![PyPI](https://img.shields.io/pypi/v/OpenRGB-PyClient?style=flat-square)](https://pypi.org/project/OpenRGB-PyClient/)
[![Read the Docs](https://img.shields.io/readthedocs/openrgb-pyclient?style=flat-square)](https://openrgb-pyclient.readthedocs.io/en/latest/)

[OpenRGB](https://gitlab.com/CalcProgrammer1/OpenRGB) 
dropped it's server protocol into master recently, so
I wrote this hacky little client library to use it.

You can find the documentation [here](https://openrgb-pyclient.readthedocs.io/en/latest/), and install it by:

```
pip install openrgb-pyclient
```

**note** This is subject to change as the library is still early in development.
I do intend to make cleaner abstractions at some point, but for now it's fairly
low level. The examples folder should contain enough code to get started, but
you'll end up having to read the source if you want to do anything more complex.
