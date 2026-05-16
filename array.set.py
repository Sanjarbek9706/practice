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

print("============== Set ================")
# set of unique collection without keeping order!
new_numbers = array("i", [1, 4, 4, 5, 7, 5, 8, 41])
numbs_set = set(new_numbers)

# print("numbs_set:", numbs_set)
print(f"the numbs_set: {numbs_set} and {type(numbs_set)}")

numbs_set.add(200)
print("numbs_set(1):", numbs_set)


numbs_set.add(7)
print("numbs_set(2):", numbs_set)

print("============== Specific operators with set ================")
#  | & - ^

a = {10, 20, 30}
b = {30, 40}

result1 = a | b  # union
result2 = a & b  # intersection
result3 = a - b  # difference
result4 = a ^ b  # simmetric difference


print("result1:", result1)
print("result2:", result2)
print("result3:", result3)
print("result4:", result4)
