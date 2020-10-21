"""
CP1404 Practicals
Renaming files
Student name: Julie-Anne Roder
"""
import os


def main():
    """Renaming file names."""
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        for filename in filenames:
            new_name = get_fixed_filename(filename)
            print("Renaming {} to {}".format(filename, new_name))
            os.rename(os.path.join(directory_name, filename), os.path.join(directory_name,new_name))


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    return new_name


# main()
