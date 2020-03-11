#!/usr/bin/python
import os
import shutil

path = r"/Users/blackout/Downloads/"
videos = r"/Users/blackout/Downloads/Videos/"
photos = r"/Users/blackout/Downloads/Photos/"
files = os.listdir(path)


for f in files:
    src = path + f
    try:
        if f[-4:] == "jpeg" or f[-3:] == "jpg" or f[-3:] == "png" or f[-4:] == "webp" or f[-3:] == "gif":
            shutil.move(src, photos)
        elif f[-4:] == "webm" or f[-3:] == "mp4":
            shutil.move(src, videos)
    except shutil.Error:
        pass
print("Done!")
