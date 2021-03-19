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
        if 'copy' in f:
            os.remove(src)  # deletes files containing the word "copy"

        elif re.search('^[\w+-]+\s?(\(\d+\))\.(jpeg|jpg|jpg_orig|jpg_large|png|webp|gif)$', f):
            os.remove(src)  # deletes duplicate photos

        elif re.search('^[\w+-]+\s?(\(\d+\))\.(webm|mp4|mkv|mov|ts)$', f):
            os.remove(src)  # deletes duplicate videos

        elif re.search('^(.+)\.(jpeg|jpg|jpg_orig|jpg_large|png|webp|gif)$', f):
            shutil.move(src, photos)  # moves photos to folder

        elif re.search('^(.+)\.(webm|mp4|mkv|mov|ts)$', f):  # everything else
            shutil.move(src, videos)  # moves videos to folder

        elif 'pdf' in f:
            shutil.move(src, pdf)  # moves pdf to folder

    except shutil.Error:
        pass

    #   deletes every leftover file
    try:
        if re.search('^(.+)\.(\w+)$', f):
            os.remove(src)
    except FileNotFoundError:
        pass
print('Done!')
