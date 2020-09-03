"""
CP1404 Practical 5
Word Occurrences program
"""

longest_word = 0
user_text = input("Text: ").lower()
words = user_text.split(" ")
words.sort()
word_count_dict = {}
for word in words:
    if len(word) > longest_word:
        longest_word = len(word)
    word_count_dict[word] = word_count_dict.get(word, 0) + 1

for key in word_count_dict:
    print("{:{}} = {}".format(key, longest_word, word_count_dict[key]))
