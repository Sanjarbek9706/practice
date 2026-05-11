'''  Objects
    (1) ECABSULATION
    (2) INHERITENCE
    (3) POLIMORHISM
'''

print("========= ECABSULATION ============")
'''
C++ JAVA >public private  protected
PHP TypeScrip > public private protected
Python > public __private _protected
'''


class Account():
    # state
    description = "The class makes bank account"

    # constructor

    def __init__(self, owner, amount):
        self.__owner = owner
        self.__amount = amount

    # method
    def get_balance(self):
        print(f"the owner {self.__owner} has {self.__amount} usd")

    def deposit(self, amount):
        print("deposit", amount)
        self.__amount += amount

    def withdraw(self, amount):
        print("withdraw:", amount)
        self.__amount -= amount

    @property
    def holder(self):
        return self.__owner

    @holder.setter
    def holder(self, new_owner):
        print("holder.setter:", new_owner)
        self.__owner = new_owner

    def change_ownership(self, new_owner):
        print("change_ownership:", new_owner)
        self.__owner = new_owner


my_account = Account("Aven", 2000)
my_account.get_balance()

print("----------")
my_account.deposit(5000)
my_account.withdraw(500)
my_account.get_balance()


# my_account.amount = 1000000
# my_account.owner = "Martin"
# my_account.amount = 10000000
# my_account.get_balance()

print("---------")

try:
    result = my_account.__amount
    print("result:", result)
except Exception as err:
    print("No target state found:", err)


# getter vs setter
# account_owner = my_account.holder  # state
print("owner before:", my_account.holder)

# my_account.change_ownership("Sanjabek") # state
my_account.holder = "SANJARBEK"  # state

print("owner after:", my_account.holder)
