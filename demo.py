# -*- coding: utf-8 -*-

from ipdb import set_trace
import sys
import io

# sys.path.insert(0, '..')
from colorthief import ColorThief
# import colorthief

IMG_FILE = '/home/jkang/project/pablo/pablo-data-processing/module-image-analysis/dev_20211226/examples_crawled/01.png'
# fd = urlopen('http://lokeshdhakar.com/projects/color-thief/img/photo1.jpg')
# f = io.BytesIO(fd.read())

color_thief = ColorThief(IMG_FILE)

print(color_thief.get_color(quality=1))
print(color_thief.get_palette(quality=1))
