"""
Read Files Programs
"""

# 1.
out_file = open("name.txt", 'w')
name = input("Your name: ")
print(name, file=out_file)
out_file.close()

# 2.
in_file = open("name.txt", 'r')
name = in_file.read()
print("Your name is {}".format(name))
in_file.close()

# 3.
in_file = open("numbers.txt", 'r')
number_1 = int(in_file.readline())
number_2 = int(in_file.readline())
total = number_1 + number_2
print("number 1 is {}, number 2 is {}, the total is {}".format(number_1, number_2, total))
in_file.close()

# 4.
in_file = open("numbers.txt", 'r')
total = 0
for line in in_file:
    total += 1
print("The total number of lines is: {}".format(total))
in_file.close()
