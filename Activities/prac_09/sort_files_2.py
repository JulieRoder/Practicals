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
    categories = []
    file_location = {}
    for directory_name, subdirectories, filenames in os.walk('.'):
        for filename in filenames:
            index = filename.find(".")
            file_extension = filename[index+1:]
            if file_extension not in file_location:
                category = get_sort_category(file_extension)
                file_location[file_extension] = category
                if category not in categories:
                    categories.append(category)
                    try:
                        os.mkdir(category)
                    except FileExistsError:
                        pass
            shutil.move(filename, file_location[file_extension])


def get_sort_category(filetype):
    """Get user input on file location."""
    category = input("What category would you like to sort {} files into? ".format(filetype))
    return category


main()
