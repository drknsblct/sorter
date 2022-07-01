#!/usr/bin/python
import os
import shutil
import re
import time

# change these to your file path on MacOS/Linux

path = r'/Users/blackout/Downloads/'  # program runs in this folder
videos_folder = r'/Users/blackout/Downloads/Media/Videos/'  # path to video folder
photos_folder = r'/Users/blackout/Downloads/Media/Photos/'  # path to image folder
pdf_folder = r'/Users/blackout/Downloads/PDF'  # path to pdf_folder folder

files = os.listdir(path)  # lists content of path folder

begin = time.time()
count = 0
deleted = 0
photos = '^(.+)\.(jpeg|jpg|jpg_orig|jpg_large|png|webp|gif)$'
videos = '^(.+)\.(webm|mp4|mkv|mov|ts|wmv)$'
duplicate_photos = '^[\w+-]+\s?(\(\d+\))\.(jpeg|jpg|jpg_orig|jpg_large|png|webp|gif)$'
duplicate_videos = '^[\w+-]+\s?(\(\d+\))\.(webm|mp4|mkv|mov|ts|wmv)$'

# create folders and skip if they already exist
os.makedirs(photos_folder, exist_ok=True)
os.makedirs(videos_folder, exist_ok=True)
os.makedirs(pdf_folder, exist_ok=True)

# count number of directories in specified path
directories = sum(os.path.isdir(os.path.join(path, i)) for i in os.listdir(path))

for f in files:
    src = path + f
    try:
        if 'copy' in f:
            os.remove(src)  # deletes files containing the word "copy"
            deleted += 1

        elif re.search(duplicate_photos, f):
            os.remove(src)  # deletes duplicate photos_folder
            deleted += 1

        elif re.search(duplicate_videos, f):
            os.remove(src)  # deletes duplicate videos_folder
            deleted += 1

        elif re.search(photos, f):
            shutil.move(src, photos_folder)  # moves photos_folder to folder
            count += 1

        elif re.search(videos, f):
            shutil.move(src, videos_folder)  # moves videos_folder to folder
            count += 1

        elif 'pdf' in f or 'epub' in f:
            shutil.move(src, pdf_folder)  # moves pdf_folder to folder
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
