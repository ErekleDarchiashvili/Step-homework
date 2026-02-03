import random

# N1_______________________________________________________________

lst = [(1, 3), (4, 2), (2, 5)]
sorted_list = sorted(lst, key=lambda x: x[1])
print(sorted_list)

# N2_______________________________________________________________

def get_random_element(length, start, end):
    lst = [random.randint(start, end) for _ in range(length)]
    try:
        index = int(input("enter an index: "))
        return lst[index]
    except IndexError:
        return "index does not exist"
    except ValueError:
        return "index must be a number"
    except Exception:
        return "an error occurred"

result = get_random_element(5, 1, 20)
print("result:", result)

# N3_______________________________________________________________

from functools import reduce

products = [
    {"name": "Laptop", "price": 1200},
    {"name": "Mouse", "price": 15},
    {"name": "Keyboard", "price": 25},
    {"name": "Monitor", "price": 150},
    {"name": "Power", "price": 100},
    {"name": "Pad", "price": 10},
]

cheap_products = list(filter(lambda p: p["price"] < 100, products))
print("products with price less than 100:", cheap_products)

names_prices = list(map(lambda p: (p["name"], p["price"]), products))
print("all product names and prices:", names_prices)

sorted_products = sorted(products, key=lambda p: p["price"])
print("products sorted by price:", sorted_products)

total_price = reduce(lambda a, b: a + b["price"], products, 0)
print("total price of all products:", total_price)


# N4_______________________________________________________________

def sum_to_n(n):
    if n == 1:
        return 1
    else:
        return n + sum_to_n(n - 1)

num = int(input("enter a number: "))
print("sum:", sum_to_n(num))
