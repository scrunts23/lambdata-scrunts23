# setup.py file

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="lambdata_ryan",  # the name that you will install via pip
    version="0.0.1",
    author="Ryan Davidson",
    author_email="scrunts23@gmail.com",
    description="Unit 3 ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # required if using a md file for long desc
    license="MIT",
    url="https://github.com/scrunts23",
    # keywords="",
    packages=find_packages()  # ["my_lambdata"]
)