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

## Development

If you would like to run this from git, you can do the following:

```
git clone https://github.com/bahorn/OpenRGB-PyClient.git
cd OpenRGB-PyClient
virtualenv -p python3 .venv
source .venv/bin/activate
pip install -r requirements.txt
```

And you can now start running scripts in `examples` like so:

`python examples/color-change.py`

## Alternatives

This isn't the only library for OpenRGBs SDK manager! You might find one of these
more suitable for your project!

* [NetworkClient.{cpp,h}](https://gitlab.com/CalcProgrammer1/OpenRGB) The C++ client in the OpenRGB repo.
* [vlakreeh's NodeJS client](https://github.com/vlakreeh/openrgb)
* [jath03's Python client](https://github.com/jath03/openrgb-python) *Currently seems be better maintained than this library*
