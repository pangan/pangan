import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    setup_requires=['pbr'],
    pbr=True,
)