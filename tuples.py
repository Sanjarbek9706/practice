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
