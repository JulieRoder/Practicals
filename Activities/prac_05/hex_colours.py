"""
CP1404 Practical 5
Student name: Julie-Anne Roder
Hex Colour Dictionary
"""

HEX_COLOUR_CODES = {"cornflowerblue": "#6495ed", "forestgreen": "#228b22", "yellow1": "#ffff00",
                    "darkorange": "#ff8c00", "firebrick2": "#ee2c2c", "mediumOrchid3": "#7a378b", "gray9": "#171717",
                    "floralwhite": "#fffaf0", "deeppink3": "#8b0a50", "saddlebrown": "#8b4513"}


def main():
    """Accessing the Hex Colour dictionary."""
    longest_colour_name = 0
    for key in HEX_COLOUR_CODES:
        print(HEX_COLOUR_CODES[key])
        if len(key) > longest_colour_name:
            longest_colour_name = len(key)

    name_of_colour = input("Enter colour name: ").lower()
    while name_of_colour != "":
        if name_of_colour in HEX_COLOUR_CODES:
            print("The colour code for {:<{}} is {:>}".format(name_of_colour, longest_colour_name,
                                                              HEX_COLOUR_CODES[name_of_colour]))
        else:
            print("Invalid colour name")
        name_of_colour = input("Enter colour name: ").lower()


main()
