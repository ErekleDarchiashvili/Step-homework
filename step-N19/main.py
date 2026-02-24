# N1_________________________________________________________________

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person: ({self.name}, {self.age})"

def serialize(person, filename):
    with open(filename, "r+") as file:
        file.write(f"Name: {person.name}, Age: {person.age}")

def deserialize(filename):
    with open(filename, "r") as file:
        line = file.readline()

    line = line.replace("Name: ", "").replace("Age: ", "")
    name, age = line.split(", ")
    return Person(name, int(age))

p1 = Person("Otar", 34)

serialize(p1, "person.txt")   

p2 = deserialize("person.txt")
print(p2)