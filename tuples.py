'''Tuple 
(1) What is tuple: typle vs list 
(2) Unpacking arguments
(3) zip
'''
print("=========== What is tuple: typle vs list ==============")
# Java/PHP/NodeJS array => Python list, boshqa tilardagi array vazifasini o'taydi


# literal
numbs = [3, 5, 6, 3]
# car_dict = {"brand": "Volvo", "year": 2027}  # dictioreni function deyiladi
# print(numbs)

#  constructor
letters = list("Hello world!")
# person_dict = dict(name="Sanjarbek", age=29)  # dictioreni function deyiladi
# print(letters)

fruits = ["apple", "lemon", "banana", "kiwi"]
print("before fruits:", fruits)

fruits[2] = "melon"
print("after fruits:",  fruits)

# tuple
# we can not mutate tuple
animals = ("dog", 'cat', "fish", "lion")
tuple_obj = ("MIT", 100, True, None)

print(animals[0])
# animals[0] = "bird"


# try avoid this
people = "Andrew", "John"
animals = "dog",


print("=========== Unpacking arguments ==============")
groups = ["MIT", "FLEXY", "DEVEX", "MG"]
(x, y, *z) = groups
print(f"the x: {x} and y: {y}")
print("z:", z)  # list


# *args > tuple
def calculate(*args):
    print("*args >", args)
    total = 1
    for x in args:
        total *= x
        print(f"the type (arge) value: {type(args)}")
        print(f"the total value: {total}")
        return total


#  CALL
calculate(1, 7, 2, 3)
print("-------")
calculate(0, 2, 300)
print("-------")
calculate(5, 7)

# **kwargs > dictionary


def introduce(**kwargs):
    print(f"the type(**kwargs)  value: {type(kwargs)}")
    print(f"Hi, I am {kwargs['name']} and I am {kwargs["age"]} years old!")
    pass


# CALL
introduce(name="Aven", age=29)
introduce(name="Gary", age=50, single=True)
print("-------")


def greeting(*args, **kwargs):
    print("*args >", args)
    print("**kwargs >", kwargs)


# CALL
greeting("Hi", True, 7, name="Aven", age=29)
