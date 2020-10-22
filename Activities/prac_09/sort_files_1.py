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
            file_extension = filename[index + 1:]
            if file_extension not in file_types:
                file_types.append(file_extension)
                try:
                    os.mkdir(file_extension)
                except FileExistsError:
                    pass
            shutil.move(filename, file_extension)


main()
