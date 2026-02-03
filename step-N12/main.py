# N1_____________________________________________________________

import os

filename = "names.txt"

if not os.path.exists(filename):
    print("file does not exist please create", filename, "first")
else:
    with open(filename, "a") as f:
        count = 1
        while True:
            first_name = input("enter your first name: ")
            if first_name.lower() == "stop":
                break
            last_name = input("enter your last name: ")
            if last_name.lower() == "stop":
                break
            f.write(f"{count}. {first_name} {last_name}\n")
            count += 1

    print("names saved in", filename)


# N2_____________________________________________________________

with open("persons.txt", "r") as f:
    lines = f.readlines()

under_50 = []
over_50 = []

for line in lines:
    parts = line.strip().split(",")
    if len(parts) >= 2:
        age = int(parts[1].strip())
        if age < 50:
            under_50.append(line)
        elif age > 50:
            over_50.append(line)

with open("under_50.txt", "w") as f:
    for person in under_50:
        f.write(person)

with open("over_50.txt", "w") as f:
    for person in over_50:
        f.write(person)

print("files 'under_50.txt' and 'over_50.txt' created successfully")

# N3_____________________________________________________________

import csv
from faker import Faker
import random

fake = Faker()
print(fake.first_name())

with open("persons.csv", "w", newline="") as f:
    fieldnames = ["ID", "first_name", "last_name", "age"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()

    for i in range(1, 51):
        writer.writerow({
            "ID": i,
            "first_name": fake.first_name().lower(),
            "last_name": fake.last_name().lower(),
            "age": random.randint(20, 80)
        })

