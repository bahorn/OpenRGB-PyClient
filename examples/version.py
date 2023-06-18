import sys, os
sys.path.append(os.path.realpath('.'))

from openrgb import OpenRGB

client = OpenRGB('localhost', 6742)

print(client.get_version())
