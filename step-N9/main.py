# N1____________________________________________________________________

def sum_numbers(times=5):
    total = 0
    for i in range(times):
        num = float(input("enter a number: "))
        total += num
    return total

result = sum_numbers()
print("total sum:", result)

# N2____________________________________________________________________

def separate_odd_even(*numbers):
    odd = []
    even = []
    for num in numbers:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    return odd, even

odds, evens = separate_odd_even(1, 2, 3, 4, 5, 6, 7)
print("Odd numbers:", odds)
print("Even numbers:", evens)

# N3____________________________________________________________________

def count_words(sentence):
    sentence = sentence.lower()
    sentence = sentence.replace(".", "").replace(",", "").replace("!", "").replace("?", "")
    words = sentence.split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

sentence = input("Enter a sentence: ")
result = count_words(sentence)
print(result)
