# ''' OBJECTS
# (1) What is object
# (2) Iterable object & RANGE
# (3) DICTIONARY
# (4) Error handling system
# '''
# import array  # package / module
# import math
# from math import ceil,  asin
# print("==========What is object============")
# # An object has state and method properties.
# # Everything is object in Python!

# print(type('Hello World!'))
# print(type(100))
# print(type(True))
# print(type(array))
# print(type(math))

# # Programming paradigms > Function Programming & OOP
# # OOP 4 CONCEPTS > Abstraction | Encapsulation | Inheritence | Polimorphism
# result1 = math.ceil(97.7)  # CALL
# print("result1:", result1)

# result2 = ceil(98.7)
# print("result2:", result2)

print("==========Error handling system============")
car_dict = dict(name="Tayota", year=2027, electric=True)

try:
    print("passed here")
    a = car_dict.speed  # AttributeError: 'dict' object has no attribute 'speed'
    result = car_dict["origin"]
    print("result:", result)
except KeyError as err:
    print("No origin state property found:", err)
except AttributeError as err:
    print("No speed found:", err)
# except (KeyError, AttributeError) as  err:
#     print("Error:",err) # qanday xatolik chiqsa shun chop etib beradi
except Exception as err:
    print("Error:", err)  # hamma xatolikni bitta tizimda akis etadi
else:
    print("Executed successfully  without errors")
finally:
    print("Final closing logic")


# result = car_dict["origin"]
# print("result:", result)
