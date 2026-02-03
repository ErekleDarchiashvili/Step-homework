class bankaccount:
    bank_name = "my bank"
    __total_accounts = 0

    @staticmethod
    def validate_amount(amount):
        return amount > 0

    @classmethod
    def get_total_accounts(cls):
        return cls.__total_accounts

    def __init__(self, owner, balance):
        self._owner = owner
        if self.validate_amount(balance):
            self.__balance = balance
        else:
            self.__balance = 0
        bankaccount.__total_accounts += 1
        self.__account_number = f"AN{bankaccount.__total_accounts:04d}"

    def deposit(self, amount):
        if self.validate_amount(amount):
            self.__balance += amount
        else:
            print("invalid amount")

    def withdraw(self, amount):
        if self.validate_amount(amount):
            if amount <= self.__balance:
                self.__balance -= amount
            else:
                print("not enough balance")
        else:
            print("invalid amount")

    def check_balance(self):
        return self.__balance

    def get_account_number(self):
        return self.__account_number

    def change_owner(self, new_owner):
        self._owner = new_owner

    def __str__(self):
        return f"account {self.__account_number} | owner {self._owner}"


acc1 = bankaccount("nino beridze", 500)
acc2 = bankaccount("john doe", 1000)

print(acc1)
print(acc2)

acc1.deposit(200)
acc1.withdraw(100)
print(acc1.check_balance())

print(bankaccount.get_total_accounts())

acc2.change_owner("mike brown")
print(acc2)
