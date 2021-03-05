#!/usr/bin/python
import os
import shutil

path = r"/Users/blackout/Downloads/"  # program runs in this folder                   change this to your file path on MacOS/Linux
videos = r"/Users/blackout/Downloads/Media/Videos/"  # path to video folder           change this to your file path on MacOS/Linux
photos = r"/Users/blackout/Downloads/Media/Photos/"  # path to image folder           change this to your file path on MacOS/Linux
pdf = r"/Users/blackout/Downloads/PDF" # path to pdf folder                           change this to your file path on MacOS/Linux

files = os.listdir(path)  # lists content of path folder

image_files = ["jpeg", "jpg", "png", "webp", "gif"]
video_files = ["webm", "mp4"]

duplicates = [x for x in range(1, 100)]  # creates a list from 1 to 99
string_duplicates = [str(x) for x in duplicates]  # makes the above list numbers to strings

for f in files:
    src = path + f
    try:
        if (f[-7:-4:2] == "()" and f[-6] in string_duplicates) or (
                f[-8:-4:3] == "()" and f[-7:-5] in string_duplicates):
            os.remove(src)  # deletes duplicate file extensions (jpg, png, gif, mp4)

        elif (f[-12:-9:2] == "()" and f[-11] in string_duplicates) or (
                f[-13:-9:3] == "()" and f[-12:-10] in string_duplicates):
            os.remove(src)  # deletes jpg_orig duplicates

        elif (f[-13:-10:2] == "()" and f[-12] in string_duplicates) or (
                f[-14:-10:3] == "()" and f[-13:-11] in string_duplicates):
            os.remove(src)  # deletes jpg_large duplicates

        elif (f[-8:-5:2] == "()" and f[-7] in string_duplicates) or (
                f[-9:-5:3] == "()" and f[-8:-6] in string_duplicates):
            os.remove(src)  # deletes duplicate file extensions (jpeg, webp, webm)

        elif "copy" in f:
            os.remove(src)  # deletes files containing the word "copy"

        elif f[-3:] in image_files or f[-4:] in image_files or ("jpg_orig" in f or "jpg_large" in f):
            shutil.move(src, photos)  # moves images to image folder

        elif f[-3:] in video_files or f[-4:] in video_files:
            shutil.move(src, videos)  # moves videos to video folder
        
        elif 'pdf' in f:
            shutil.move(src, pdf)
        
        elif "dmg" in f:
            os.remove(src)

    except shutil.Error:
        pass

# delete photo/video/pdf from Downloads if already in Photo/Video folder
    try:
        if f[-3:] in image_files or f[-4:] in image_files or ("jpg_orig" in f or "jpg_large" in f) or f[-3:] in video_files or f[-4:] in video_files:
            os.remove(src)
        elif "pdf" in f:
            os.remove(src)
    except FileNotFoundError:
        pass
print("Done!")