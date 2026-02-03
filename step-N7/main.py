# N1____________________________________________________________________________

persons = [
    ('Kelly', 'Simpson', 26),
    ('Erika', 'Stephens', 24),
    ('Cheryl', 'Dunn', 30),
    ('Amy', 'Larsen', 49),
    ('Christine', 'Gordon', 23),
    ('Monica', 'Huff', 38),
    ('David', 'Nixon', 36),
    ('Cindy', 'Escobar', 41),
    ('Cindy', 'White', 33),
    ('Joel', 'Hall', 43),
    ('Steven', 'Winters', 28),
    ('Alex', 'Cole', 68),
    ('Alex', 'Smith', 32),
    ('Brittany', 'Thompson', 18),
    ('Ernest', 'Young', 43),
    ('Traci', 'Wells', 38),
    ('Andrew', 'Flores', 61),
    ('Christopher', 'Lewis', 29),
    ('Kevin', 'Willis', 57),
    ('Kayla', 'Lucas', 28),
    ('Michelle', 'Rush', 43),
    ('Thomas', 'Mason', 37)
]

while True:
    first_name = input("enter your first name (or 'stop' to quit): ").strip()
    if first_name.lower() == "stop":
        print("exiting program")
        break

    found_first = False
    for person in persons:
        if person[0].lower() == first_name.lower():
            found_first = True
            break

    if not found_first:
        print("no such first name found")
        continue

    last_name = input("enter your last name: ").strip()
    found_last = False
    for person in persons:
        if person[0].lower() == first_name.lower() and person[1].lower() == last_name.lower():
            print(f"{first_name} {last_name} is {person[2]} years old.")
            found_last = True
            break

    if not found_last:
        print("no such last name found")


# N2____________________________________________________________________________

word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")

set1 = set(word1)
set2 = set(word2)

common_chars = set1 & set2
different_chars = set1 ^ set2
combined_chars = set1 | set2

print("Common characters:", common_chars)
print("Different characters:", different_chars)
print("Combined characters:", combined_chars)
