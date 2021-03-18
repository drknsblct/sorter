#!/usr/bin/python
import os
import shutil
import re

# change these to your file path on MacOS/Linux

path = r'/Users/blackout/Downloads/'  # program runs in this folder
videos = r'/Users/blackout/Downloads/Media/Videos/'  # path to video folder
photos = r'/Users/blackout/Downloads/Media/Photos/'  # path to image folder
pdf = r'/Users/blackout/Downloads/PDF'  # path to pdf folder

files = os.listdir(path)  # lists content of path folder

for f in files:
    src = path + f
    try:
        if re.search('^\w+\(?\d+\)?\.(jpeg|jpg|png|webp|gif)', f):
            os.remove(src)

        elif re.search('^\w+\(?\d+\)?\.(webm|mp4|mov)', f):
            os.remove(src)

        elif 'copy' in f:
            os.remove(src)  # deletes files containing the word "copy"

        elif re.search('^\w+\.(jpeg|jpg|png|webp|gif)', f):
            shutil.move(src, photos)

        elif re.search('^\w+\.(webm|mp4|mov)', f):
            shutil.move(src, videos)

        elif 'pdf' in f:
            shutil.move(src, pdf)

        elif "dmg" in f:
            os.remove(src)

        elif 'crdownload' in f:
            os.remove(src)

    except shutil.Error:
        pass

    # delete every leftover file that isn't a folder
    try:
        if re.search('^\w+\.\w+\.?\w+$', f):
            os.remove(src)
    except FileNotFoundError:
        pass
print('Done!')
