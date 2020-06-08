import setuptools
import os

# bump this regularly.
default_version = "0.0.1"

with open("README.md", "r") as fh:
    long_description = fh.read()

# Either extract it from the release trigger, or use the default version.
version = os.environ['GITHUB_REF'].split('/')[-1][1:] or default_version

setuptools.setup(
    name="OpenRGB-PyClient",
    version=version,
    author="B Horn",
    author_email="b@horn.uk",
    description="Python Client for the OpenRGB SDK Server",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bahorn/OpenRGB-PyClient",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    setup_requires=['wheel']
)
