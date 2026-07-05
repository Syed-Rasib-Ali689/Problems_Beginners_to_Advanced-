"""
Takes a sentence (a string) as input from the user.
Counts how many times each word appears, ignoring case (e.g., "The" and "the" should count as the same word).
Prints each unique word along with its frequency, sorted from most frequent to least frequent.
If two words have the same frequency, their relative order does not matter.
"""
# Taking input from user
sentence = input("Enter a sentence: ")

# Convereting string in lower case
sentence = sentence.lower()

#  Spliting Sentense in list
split_sentence = sentence.split()

# Main logic or Core
word_count = {}

for word in split_sentence:
    if word in word_count:
        word_count[word] +=1
    else:
        word_count[word] = 1

# Sorting Words 
sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
for word, count in sorted_words:
    print(f"{word}: {count}")