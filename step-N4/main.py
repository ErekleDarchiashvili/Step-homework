# N1______________________________________________________________________________

sentence = input("Enter a sentence: ")
first_word = input("Enter the word to replace: ")
second_word = input("Enter the new word: ")

new_sentence = sentence.replace(first_word, second_word)

print("updated sentence:")
print(new_sentence)

# N2______________________________________________________________________________

sentence1 = input("Enter a sentence: ")

words = sentence1.split()

longest_word = ""

for word in words:
    if len(word) > len(longest_word):
        longest_word = word

print("the longest word is:", longest_word)

# N3______________________________________________________________________________

word1 = input("Enter first word: ").lower()
word2 = input("Enter second word: ").lower()

if len(word1) != len(word2):
    print("Not anagrams")
else:
    is_anagram = True

    for char in word1:
        if word1.count(char) != word2.count(char):
            is_anagram = False
            break

    if is_anagram:
        print("the words are anagrams")
    else:
        print("the words are not anagrams")

