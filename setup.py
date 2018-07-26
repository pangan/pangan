import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    setup_requires=['pbr'],
    pbr=True,
    name="pangan",
    author="Amir Mofakhar",
    author_email="amir@mofakhar.info",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pangan/pangan",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)