"""
Write a Python program with two separate functions:
Function 1: is_palindrome(text)
Function 2: is_anagram(word1, word2)
"""

def is_palindrome(text):
    cleaned = ""
    for char in text.lower():
        if char.isalpha():
            cleaned += char
    return cleaned == cleaned[::-1]

def is_anagram(word1, word2):
    return sorted(word1.lower()) == sorted(word2.lower())


print("*" * 50)
print("Welcome to Word Checker")
print("1 for checking if a sentence is a palindrome")
print("0 for checking if two words are anagrams")
print("-" * 50)

choice = int(input("Enter 1 or 0: "))

if choice == 1:
    sentence = input("Enter a sentence to check: ")
    result = is_palindrome(sentence)
    print("Is Palindrome:", result)

elif choice == 0:
    word1 = input("Enter word 1: ")
    word2 = input("Enter word 2: ")
    result = is_anagram(word1, word2)
    print("Is Anagram:", result)

else:
    print("Invalid choice. Please enter 1 or 0.")