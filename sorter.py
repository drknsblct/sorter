#!/usr/bin/python
import os
import shutil
import re
import time

# change these to your file path on MacOS/Linux

path = r'/Users/blackout/Downloads/'  # program runs in this folder
videos = r'/Users/blackout/Downloads/Media/Videos/'  # path to video folder
photos = r'/Users/blackout/Downloads/Media/Photos/'  # path to image folder
pdf = r'/Users/blackout/Downloads/PDF'  # path to pdf folder

files = os.listdir(path)  # lists content of path folder

begin = time.time()
count = 0
deleted = 0

try:
    os.makedirs(photos, exist_ok=True)
    os.mkdir(videos)
except OSError:
    pass

# create pdf folder
try:
    os.mkdir(pdf)
except OSError:
    pass

# count number of directories in specified path
directories = sum(os.path.isdir(os.path.join(path, i)) for i in os.listdir(path))

for f in files:
    src = path + f
    try:
        if 'copy' in f:
            os.remove(src)  # deletes files containing the word "copy"
            deleted += 1

        elif re.search('^[\w+-]+\s?(\(\d+\))\.(jpeg|jpg|jpg_orig|jpg_large|png|webp|gif)$', f):
            os.remove(src)  # deletes duplicate photos
            deleted += 1

        elif re.search('^[\w+-]+\s?(\(\d+\))\.(webm|mp4|mkv|mov|ts)$', f):
            os.remove(src)  # deletes duplicate videos
            deleted += 1

        elif re.search('^(.+)\.(jpeg|jpg|jpg_orig|jpg_large|png|webp|gif)$', f):
            shutil.move(src, photos)  # moves photos to folder
            count += 1

        elif re.search('^(.+)\.(webm|mp4|mkv|mov|ts)$', f):
            shutil.move(src, videos)  # moves videos to folder
            count += 1

        elif 'pdf' in f or 'epub' in f:
            shutil.move(src, pdf)  # moves pdf to folder
            count += 1

    except shutil.Error:
        pass

    # deletes every leftover file
    try:
        if re.search('^(.+)\.(\w+)$', f):
            os.remove(src)
    except FileNotFoundError:
        pass

print(f'Time elapsed for {count} items: {time.time() - begin :.2f} seconds')

if deleted > 0:
    print(f'Items deleted: {deleted}')
