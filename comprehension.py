''' Comprehension
    (1) What is comprehersion & list comp.
    (2) set and dictionary comp.
'''


print("======= What is comprehersion & list comprehsion ========")
# comprehension  acts like spread operator!

''' Comperehsion general syntax:
    (a) *iterable
    (b) <expression> for item in iterable
    (c) <expression> for item in iterable <condition> 
'''

# list comp.
numbers = [1, 2, 4, 2, 1, 34]
# list_numbers = [*numbers]  # a version
list_numbers = numbers  # a version

print("list_numbers:", list_numbers)
print(numbers is list_numbers)
print(id(numbers), id(list_numbers))


print("----------------")
people = [("Rebord", 22), ("Steve", 19), ("Aven", 29)]
list_people = [person[0] for person in people]  # b version
print("list_people:", list_people)

cars = [
    ("Ferrari", 78),
    ("Tayota", 87),
    ("Audi",  116),
    ("BWM", 109),
    ("Pagani", 33),
    ("Volvo", 99)
]
list_cars = [car[0] for car in cars if car[1] > 80]  # c version
print("list_cars:", list_cars)


print("======= set and dictionary comprehension ========")
numbs = [1, 5, 2, 4, 30, 5, 3, 2]
set_numbs = {*numbs}
print("set_numbs:", set_numbs)

dict_people = {person[0]: person[1] for person in people}  # b version
print("dirc_)people:", dict_people)

dict_people2 = {person[0]: person[1]
                for person in people if person[1] > 20}  # c version
print("dirc_)people2:", dict_people2)
