print("========= number ==========")
# in JAVA, variable is a name  storage location!
# in Python, varible is a named reference!

count = 100
count_type = type(count)
# print("count:", count, count_type)
print(f"the count: {count} and type: {count_type}")

result1 = count.bit_count()  # method
resilt2 = count.numerator  # state
print(result1, resilt2)

print("========= string ==========")
# METHODS: upper() lower() title() find() replace()

course = "AI Python FullStack"
result = type(course)
print(f"the result (1): {result}")  # the result (1): <class 'str'>

result = course.title()
print(f"the result (2): {result}")  # the result (2): Ai Python Fullstack

result = course.upper()
print(f"the result (3): {result}")  # the result (3): AI PYTHON FULLSTACK

result = course.replace("FullStack", "MasterClass")
print(f"the result (4): {result}")  # the result (4): AI Python MasterClass


print("========= boolean ==========")
# function > type() input() bool() int() str()
y = input("give your value for y: ")
print("y:", y)

result = y.isnumeric()  # raqam kiritilsin
print(f"the input value is numeric: {result}")

# TRUTHY vs FALSY value
# TRUTHY: true 100 -100 "AVEN"
# FALSY: false 0 "" None

test_falsy = "" or False or None or 0
print("The FALSY:", bool(test_falsy))

test_truthy = "AVEN"
print("test_truthy:", bool(test_truthy))
