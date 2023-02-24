#!/usr/bin/env python
"""
Calibrate raw images (DNG or CR3) with an input color profile (..)

..
"""
from pathlib import Path
from enum import Enum


class ImageFormat(str, Enum):
    DNG = "DNG"
    CR3 = "CR3"


class Calibrate(object):
    """
    ..
    """
    def __init__(
            self,
            darktable_cli: Path,
            input_dir: Path,
            output_dir: Path,
            icc_file: Path,
            image_format: ImageFormat):
        self.darktable_cli = darktable_cli
        self.input_dir = input_dir
        self.output_dir = output_dir
        self.icc_file = icc_file
        self.image_format = image_format

    def run(self):
        """ use subprocess to call darktable-cli to calibrate the images"""

