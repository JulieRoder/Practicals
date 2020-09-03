"""
CP1404 Practical 5
Word Occurrences program
"""


text = input("Text: ")
words = text.split(" ")
word_count_dict = {}
for word in words:
    word_count_dict[word] = word_count_dict.get(word, 0) + 1

print(word_count_dict)
