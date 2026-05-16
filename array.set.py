''' Array & Set
    (1) Array
    (2) Set
    (3) Specific operators with set
'''
from array import array
print("============== Array ================")
numbers = array("i", [1,  2, 3, 4, 5, 6, 7, 53])
print("numbers(1):", numbers)

numbers.append(100)
numbers.insert(0, 14)
print("numbers(2):", numbers)

numbers.remove(7)
numbers.pop()
print("numbers(3):", numbers)

del numbers[0:2]
print("numbers(4):", numbers)
