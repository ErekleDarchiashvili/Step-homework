# 1N____________________________________________________________

def file_info(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
    line_count = len(lines)
    longest_line = max(lines, key=len).strip()
    word_count = sum(len(line.split()) for line in lines)
    return line_count, longest_line, word_count

filename = input("enter filename: ")
lines, longest, words = file_info(filename)
print("lines:", lines)
print("longest line:", longest)
print("words:", words)

# 2N____________________________________________________________

def count_word_in_file(filename, word):
    count = 0
    with open(filename, "r") as f:
        for line in f:
            words = line.lower().split()
            count += words.count(word.lower())
    return count

filename = input("enter filename: ")
word = input("enter word: ")
print("count:", count_word_in_file(filename, word))
