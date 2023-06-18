import sys, os
sys.path.append(os.path.realpath('.'))

from openrgb import OpenRGB

client = OpenRGB('localhost', 6742)

profiles = client.profiles()
print(profiles)

client.load_profile(profiles[0])
