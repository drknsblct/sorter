#!/usr/bin/python
import os
import shutil

path = r"/Users/blackout/Downloads/" #program runs in this folder                   change this to your file path on MacOS/Linux
videos = r"/Users/blackout/Downloads/Media/Videos/" #path to video folder           change this to your file path on MacOS/Linux
photos = r"/Users/blackout/Downloads/Media/Photos/" #path to image folder           change this to your file path on MacOS/Linux

files = os.listdir(path) #lists content of path folder

image_files = ["jpeg", "jpg", "png", "webp", "gif"]
video_files = ["webm", "mp4"]

duplicates = [x for x in range(1, 100)] #creates a list from 1 to 99
string_duplicates = [str(x) for x in duplicates] #makes the above list numbers to strings

for f in files:
    src = path + f
    try:
        if (f[-7:-4:2] == "()" and f[-6] in string_duplicates) or (f[-8:-4:3] == "()" and f[-7:-5] in string_duplicates):
              os.remove(src) #delete duplicate file extensions (jpg, png, gif, mp4)

        elif (f[-8:-5:2] == "()" and f[-7] in string_duplicates) or (f[-9:-5:3] == "()" and f[-8:-6] in string_duplicates):
            os.remove(src) #delete duplicate file extensions (jpeg, webp, webm)

        elif "copy" in f:
            os.remove(src) #delete files containing the word "copy"

        elif f[-3:] in image_files or f[-4:] in image_files:
            shutil.move(src, photos) #moves images to image folder

        elif f[-3:] in video_files or f[-4:] in video_files:
            shutil.move(src, videos) #moves videos to video folder

    except shutil.Error:
        pass
print("Done!")





