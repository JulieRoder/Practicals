"""
CP1404 Practicals
Sorting files 1
Student name: Julie-Anne Roder
"""
import os
import shutil


def main():
    """Sort files."""
    os.chdir('FilesToSort')
    file_types = []
    for directory_name, subdirectories, filenames in os.walk('.'):
        for filename in filenames:
            index = filename.find(".")
            if filename[index+1:] not in file_types:
                file_types.append(filename[index+1:])
                os.mkdir(filename[index+1:])
            shutil.move(filename, filename[index+1:])


main()
