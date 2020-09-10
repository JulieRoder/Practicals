"""
Random Numbers
"""

import random
print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

# What did you see on line 1?
# smallest: 10, largest: 20, smallest possible is 5.
# What did you see on line 2?
# smallest: 3, largest: 9, got a lot of 5's.
# Could line 2 have produced a 4?
# no, because range is set for odd numbers.
# What did you see on line 3?
# smallest: 2.859181026094012
# largest:  5.266427815701068

print(random.randint(1, 100))  # will produce random integer between 1-100 inclusive
print(random.randrange(1, 101))  # will produce random integer between 1-100 inclusive
print(random.uniform(1, 100))  # will produce random multi-decimal numbers between 1-100, inclusive with rounding
