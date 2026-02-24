# N1___________________________________________________________________

def commission_decorator(func):
    def wrapper(balance, amount):
        commission = 1
        total = amount + commission
        
        if balance < total:
            return "error: Not enough money in the account."
        
        return func(balance - commission, amount)
    
    return wrapper


@commission_decorator
def transaction(balance, amount):
    return balance - amount


print(transaction(100, 20))   
print(transaction(10, 10))    

# N2___________________________________________________________________

class checkMethods(type):
    def __new__(cls, name, bases, dct):
        for key, value in dct.items():
            if callable(value):
                if not key.startswith("_"):
                    raise ValueError(f"method '{key}' must start with '_'")
        return super().__new__(cls, name, bases, dct)

class GoodClass(metaclass=checkMethods):
    def _test(self):
        print("Valid method")

    x = 10

class BadClass(metaclass=checkMethods):
    def test(self):
        print("Invalid")
