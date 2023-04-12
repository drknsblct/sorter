#!/usr/bin/python
import os
import shutil
import re
import time

# Set folder paths
path = r'/Users/blackout/Downloads/'
media_folder = r'/Users/blackout/Downloads/Media/'
videos_folder = os.path.join(media_folder, 'Videos/')
photos_folder = os.path.join(media_folder, 'Photos/')
pdf_folder = r'/Users/blackout/Downloads/PDF/'

# Get a list of files in the specified directory
files = os.listdir(path)

# Initialize counters and start the timer
begin = time.time()
count = 0
deleted = 0

# Define regex patterns for file types
file_patterns = {
    'photos': re.compile(r'^(.+)\.(?:jpeg|jpg(?:_orig|_large)?|png|webp|gif)$'),
    'videos': re.compile(r'^(.+)\.(?:webm|mp4|mkv|mov|ts|wmv)$'),
    'duplicates': re.compile(r'^[\w+-]+\s?(\(\d+\))\.(?:jpeg|jpg(?:_orig|_large)?|png|webp|gif|webm|mp4|mkv|mov|ts|wmv)$'),
}

# Define target folders for different file types
folder_paths = {
    'photos': photos_folder,
    'videos': videos_folder,
    'pdfs': pdf_folder,
}

# Create folders if they do not exist
for folder in folder_paths.values():
    os.makedirs(folder, exist_ok=True)

# Count the number of directories in the specified path
directories = sum(os.path.isdir(os.path.join(path, i)) for i in os.listdir(path))

# Iterate through the files in the directory
for f in files:
    src = os.path.join(path, f)

    try:
        # Remove files containing 'copy' or matching duplicate patterns
        if 'copy' in f or file_patterns['duplicates'].search(f):
            os.remove(src)
            deleted += 1

        # If the file isn't a duplicate, move it to the appropriate folder
        else:
            for filetype, pattern in file_patterns.items():
                if pattern.search(f):
                    shutil.move(src, folder_paths[filetype])
                    count += 1
                    break

            # Move PDFs and EPUBs to their designated folder
            else:
                if 'pdf' in f or 'epub' in f:
                    shutil.move(src, pdf_folder)
                    count += 1

    # Handle errors and file not found exceptions
    except (shutil.Error, FileNotFoundError):
        pass

# Print the summary of the operation
print(f'Time elapsed for {count} items: {time.time() - begin :.2f} seconds')

# Print the number of deleted items, if any
if deleted > 0:
    print(f'Items deleted: {deleted}')

