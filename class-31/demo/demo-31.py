#!/usr/bin/env python3

from sys import platform
import os
from glob import glob

def do_linux_stuff():
    directory = "." # prompt user
    whichFile = "*.png" # prompt
    # os.system("find " + str(directory) + ' -type f -name "' + str(whichFile) + "\" -print | echo \"Found $(grep -c /) files that matched:\"")
    os.system(f"find {directory} -type f -name '{whichFile}' -print | echo Found $(grep -c /) files that matched:")

def do_windows_stuff():
    directory = "." # prompt user
    whichFile = "*.png" # prompt 
    searchCount = os.popen("dir /a:-d /s /b " + str(directory) + " | find /c \":\\\"").read()


def do_cross_platform_stuff():
    """print out all images found
    Image = something.png for now
    Look for any pngs vs. examining each file
    """
    # print(help(os.walk))
    directory = "." # prompt user
    file_patterns = ["*.png","image_a*.jpg"] # prompt user (will need to convert user input to list)

    matched_files = []

    for dirpath, dirnames, filenames in os.walk(directory):
        for file_pattern in file_patterns:
            current_matched_files =  glob(dirpath + "/" + file_pattern)
            matched_files += current_matched_files
            # append will make nested lists, concat will append item by item

    matched_count = len(matched_files)
    print(f"Found {matched_count} files.")
    return matched_files

# would like to run do_linux_stuff when executing on Linux, do_windows_stuff when on Windows

# if platform == "windows":
#     do_windows_stuff()
# else:
#     do_linux_stuff()

matched = do_cross_platform_stuff()
print(matched)