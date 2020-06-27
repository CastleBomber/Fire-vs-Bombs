#!/usr/bin/env python

'''
    my implementation of hzeller's image-viewer

    will tweak around with options

    goal: 64x64
'''
import time
import sys
from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image

options = RGBMatrixOptions()
options.rows = 64 # works
optinos.cols = 64 #
options.chain_length = 1
options.parallel = 1
options.hardware_mapping = 'adafruit-hat'

image = Image.open(image_file)
matrix = RGBMatrix(options = options)
image.thumbnail((matrix.width, matrix.height), Image.ANTIALIAS)
matrix.SetImage(image.convert('RGB'))

try:
    print("Press CTRL-C to stop.")
    while True:
        time.sleep(100)
except KeyboardInterrupt:
    sys.exit(0)
