# N1_____________________________________________________________________

squares = {i: i * i for i in range(1, 11)}

print("dictionary of numbers and their squares:")
print(squares)

# N2_____________________________________________________________________

products = [
    {"cola": {"price": 1.5, "quantity": 10}},
    {"fanta": {"price": 2.5, "quantity": 5}},
    {"snickers": {"price": 3.5, "quantity": 12}},
    {"water": {"price": 4.5, "quantity": 8}},
    {"beer": {"price": 6.5, "quantity": 5}}
]

print("product names:")
for product in products:
    for name in product.keys():
        print(name)

total_cost = 0
for product in products:
    for details in product.values():
        total_cost += details["price"] * details["quantity"]

print("total cost of all products:", total_cost)

# N3_____________________________________________________________________

fruit_counts = {}

while True:
    fruit = input("Enter your favorite fruit: ").lower() 
    if fruit == "stop":
        break

    if fruit in fruit_counts:
        fruit_counts[fruit] += 1

    else:
        fruit_counts[fruit] = 1

print("Result:", fruit_counts)

