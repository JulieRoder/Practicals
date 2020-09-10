"""
Looping programs
"""

# Print odd numbers between 1 and 20
for i in range(1, 21, 2):
    print(i, end=" ")
print()

# Counting in 10s from 0 to 100
for i in range(0, 101, 10):
    print(i, end=" ")
print()

# Counting down from 20 to 1
for i in range(20, 0, -1):
    print(i, end=" ")
print()

# Print user given number of stars
number_of_stars = int(input("Number of stars: "))
for i in range(number_of_stars):
    print("*", end="")
print()

# Print user given number lines of increasing stars
number_of_stars = int(input("Number of stars: "))
for i in range(number_of_stars + 1):
    print("*" * i)
print()
