'''List
   (1) Working with lists
   (2) List methods
   (3) Lambda function
   (4) enumerate, map and filter
'''

print("========== Working with lists ===========")
# Java/PHP/NodeJS array => Python list

# Literal
person = {"name": "Justin", "age": 25}  # dictionary
person = {"Andrew", "John", "Michael"}  # tuple
groups = {"MIT", "FLEXY", "DEVEX", "MG"}  # list
for team in groups:
    print(f"the team: {team}")


# constructor
letters = list("Hello World!")
print(f"the letters:  {letters} and size: {len(letters)}")


print("---------")
fruits = ["apple", "orange", "lemon", "kiwi"]
a = fruits[0]
b = fruits[0:3]  # [0, 3)
c = fruits[::3]
d = fruits[::-1]

print("a:", a)
print("b:", b)
print("c:", c)
print("d:", d)


print("========== List methods ===========")
# methods > append()  insert() pop() remove() clear() sort() index()

letters = ["a", "d", "b"]

letters.append("c")  # add behind
print(f"the appent result: {letters}")


letters.insert(0, "z")  # add  front
print(f"the insert result: {letters}")

size = len(letters) - 1
result1 = letters.pop(size)  # pop behind
print(f"the pop result1: {result1} and letters: {letters}")

result2 = letters.pop(0)  # pop frond
print(f"the pop result2: {result2} and letters: {letters}")


print("--------------")
animals = ["dog", "cat", "capybara", "fish", "lion"]
print("animals:", animals)

animals.remove("lion")
print("animals remove:", animals)

del animals[2:4]
print("animals delete:", animals)

exist = animals.index("cat")
print("cat exist:", exist)


animals.clear()
print("animals clear:", animals)

if "cat" in animals:
    print("index of cat:", animals.index("cat"))
else:
    print("cat does not exist")


print("---------")
numbers = [2, 30, 21, 7, 87]
numbers.sort()
print("sort default:", numbers)
numbers.sort(reverse=True)
print("sort reverse:", numbers)


# immutable sorted
numbers = [2, 20, 12, 199]
new_numbers = sorted(numbers)
print(f"the sorted numbers: {numbers} and new_numbers: {new_numbers}")


print("========== Lambda function ===========")
#  lambda  is small anonymous function!


def calculate(x, y): return x * y


result = calculate(3, 5)
print("result:", result)


people = [
    ("Robert", 20),
    ("Steve", 18),
    ("Joseph", 30),
    ("Michaeel", 40),
    ("Ali", 60)
]

people.sort()
print("peaople(1)", people)


# sort by age via lambda
people.sort(key=lambda person: person[1])
print("people(2)", people)


print("========== enumerate, map and filter ===========")
# enumerate for index & value

animals = ["dog", "cat", 'fish']
for element in enumerate(animals):
    print("element:", element)

print("-------------")
for (index, value) in enumerate(animals):
    print(f"the index:  {index} and value: {value}")

print("-------------")
# similar in dictionaries
car_obj = dict(brand="Volvo", year=2027)  # dict
result = car_obj.items()
for (key, value) in result:
    print(f"the key: {key} and  value: {value}")


print("-------------")
cars = [
    ("Ferrari", 78),
    ("Tayota", 87),
    ("Audi",  116),
    ("BWM", 109),
    ("Pagani", 33),
    ("Volvo", 99)
]

new_cars = []
for car in cars:
    new_cars.append(car[0])
print("new_car(1):", new_cars)

# map
result_map = map(lambda car: car[0], cars)
print(f"the result1: {result1} and type: {type(result1)}")

new_cars = list(result1)
print("new_cars(2)", new_cars)


print("-------------")
# filter
result_filter = filter(lambda car: car[1] > 97, cars)
print(f"the result_filter: {result_filter}and type: {type(result_filter)}")
print(list(result_filter))
