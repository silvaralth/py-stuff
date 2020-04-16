# @sivlaralth
# Sergio Ballen

# pip3 install Pillow
from __future__ import print_function
import glob, os
# import os, sys
from PIL import Image

size = (128, 128)

#read sys -> python3 image.py file.xxx
def runSys ():
  print(':D')
  for infile in sys.argv[1:]:
    f, e = os.path.splitext(infile)
    outfile = f + ".jpg"
    if infile != outfile:
      try:
        Image.open(infile).save(outfile)
      except IOError:
          print("cannot convert", infile)

# read folder .jpg's
def run ():
  for infile in glob.glob("*.jpg"):
    file, ext = os.path.splitext(infile)
    im = Image.open(infile)
    im.thumbnail(size)
    im.save(file + "_small.jpg", "JPEG")

if __name__ == '__main__':
  run()