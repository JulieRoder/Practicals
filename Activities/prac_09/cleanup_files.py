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
            os.rename(os.path.join(directory_name, filename), os.path.join(directory_name, new_name))


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    temp_name = filename.replace(".TXT", ".txt")
    if " " not in temp_name:
        spaced_name = add_space(temp_name)
    elif " " not in temp_name[:6]:
        spaced_name = add_space(temp_name)
        spaced_name = spaced_name.title()
    else:
        spaced_name = filename.title()
    new_name = spaced_name.replace(" ", "_").replace(".Txt", ".txt")
    return new_name


def add_space(filename):
    """Add spaces to titles."""
    capitals, capitals_count = determine_spacing(filename)
    if capitals_count == 4:
        new_name = filename[:capitals[0]] + " " + filename[capitals[0]:capitals[1]] + " " + \
                   filename[capitals[1]:capitals[2]] + " " + filename[capitals[2]:capitals[3]] + " " + \
                   filename[capitals[3]:]
    elif capitals_count == 3:
        new_name = filename[:capitals[0]] + " " + filename[capitals[0]:capitals[1]] + " " + \
                   filename[capitals[1]:capitals[2]] + " " + filename[capitals[2]:]
    elif capitals_count == 2:
        new_name = filename[:capitals[0]] + " " + filename[capitals[0]:capitals[1]] + " " + filename[capitals[1]:]
    elif capitals_count == 1:
        new_name = filename[:capitals[0]] + " " + filename[capitals[0]:]
    else:
        new_name = filename
    return new_name


def determine_spacing(filename):
    """Determine where spaces are to be added."""
    capitals = []
    capitals_count = 0
    for i, character in enumerate(filename):
        if character.isupper() and i > 0:
            capitals.append(i)
            capitals_count += 1
    return capitals, capitals_count


def tests():
    """Testing function."""
    filename = "AllTheGoodThings.TXT"
    determine_spacing(filename)
    new_name = get_fixed_filename(filename)
    print(new_name)
    filename2 = "over the hill.txt"
    determine_spacing(filename2)
    new_name = get_fixed_filename(filename2)
    print(new_name)
    filename3 = "ItIsWell (oh my soul).txt"
    determine_spacing(filename3)
    new_name = get_fixed_filename(filename3)
    print(new_name)


main()
# tests()
