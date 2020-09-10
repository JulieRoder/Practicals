"""
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Extract data and print details"""
    data = get_data()
    print_details(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    list_of_parts = []
    input_file = open(FILENAME)
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        print("----------")
        list_of_parts.append(parts)
    input_file.close()
    return list_of_parts


def get_longest_name(list_file):
    """Get length of longest name"""
    longest_name = 0
    for parts in list_file:
        if len(parts[1]) > longest_name:
            longest_name = len(parts[1])
    return longest_name


def print_details(list_file):
    """Printing details from list"""
    longest_name_length = get_longest_name(list_file)
    for parts in list_file:
        print("{} is taught by {:<{}} and has {:>3} students".format(parts[0], parts[1], longest_name_length,
                                                                     parts[2]))


main()
