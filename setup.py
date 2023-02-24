#!/usr/bin/env python

"""
Setup file for installing autophotogram.

pip installation for developers:
cd autophotogram
pip install -e .
"""

import re
from setuptools import setup, find_packages


# get version from __init__.py
INITFILE = "autophotogram/__init__.py"
CUR_VERSION = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                    open(INITFILE, "r").read(),
                    re.M).group(1)


# run setup
setup(
    name="autophotogram",
    version=CUR_VERSION,
    url="https://github.com/eaton-lab/photogram",
    author="",
    author_email="",
    description="An automate pipeline for photogrammetry data preparing",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=[
        "requests",
        "typer",
    ],
    entry_points={
        "console_scripts": ["autophotogram = autophotogram.__main__:app"]
    },
    license='GPL',
    classifiers=[
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',                
    ],
)