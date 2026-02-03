class student:
    def __init__(self, first_name, last_name, age, grades):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.grades = grades
        self.status = True
        self.fee = 1000

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_discount(self):
        if self.age > 18:
            return self.fee * 0.8
        return self.fee

    def calculate_average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def get_status(self):
        avg = self.calculate_average()
        if avg > 90:
            return "excellent"
        elif 70 < avg <= 90:
            return "good"
        elif 50 < avg <= 70:
            return "average"
        else:
            self.status = False
            return "poor"

student1 = student("john", "doe", 19, [95, 85, 90])
print(student1.get_full_name())
print(student1.get_discount())
print(student1.calculate_average())
print(student1.get_status())
print(student1.status)
