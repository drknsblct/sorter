# Sorter

A simple Python script to organize files in a directory by moving them to appropriate folders based on their file types.

## Features

- Organizes photos, videos, and PDFs/EPUBs.
- Deletes duplicate files and files containing the word "copy".
- Provides a summary of the operation, including time elapsed and items deleted.

## Requirements

- Python 3.x

## Usage

1. Update the folder paths in the script to match your desired file paths:

   - `path`: The folder containing files to be organized.
   - `media_folder`: The parent folder for media files (photos and videos).
   - `photos_folder`: The folder for photos.
   - `videos_folder`: The folder for videos.
   - `pdf_folder`: The folder for PDFs and EPUBs.

2. Save and run the script using Python:
python sorter.py


## How it Works

Sorter scans the specified directory (`path`) and performs the following actions:

1. Deletes files containing the word "copy" or matching duplicate file patterns.
2. Moves photos to the `photos_folder`.
3. Moves videos to the `videos_folder`.
4. Moves PDFs and EPUBs to the `pdf_folder`.

After processing all files, Sorter prints the time elapsed for the operation and the number of items deleted.

## Limitations

- Sorter assumes a specific set of file extensions for photos and videos. If you need to include additional file types, update the regex patterns in `file_patterns`.
- It does not handle files with the same name in the destination folder, which may result in an error or file overwriting.
