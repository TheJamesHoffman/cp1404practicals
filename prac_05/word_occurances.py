word_to_count = {}
text = input("Please enter a sentence or series of words: ")
words_in_count = text.split()
for words in words_in_count:
    try:
        frequency = words_in_count
        word_to_count[words] += 1
    except KeyError:
        word_to_count[words] = 1


words_in_count = list(word_to_count.keys())
words_in_count.sort()
print(word_to_count)

max_length = max((len(word) for word in word_to_count))
for words in word_to_count:
    print("{:{}} : {}".format(words, max_length, word_to_count[words]))
