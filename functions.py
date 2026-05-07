''' FUNCTIONLAR > DARS REJASI:
1) Functionlarning Define va Call jarayoni
2) Parametr va Argument
3) Keyword va Default argumentlar
4)Functionlarda Scope tushunchasini organamiz
'''
print("=========DEFINE (parameter )vs CALL (argument) ============")
# build in function > print() type()
# Function - reusable block of code!
# Instead of block {} in JAVA, Python use indentation!


# DEFINE - build -parameter
def greet(a):  # void function qiymat qaytarmaydi
    print(f"How do you do, {a}")


# return functiom qiymat qaytaradi
def greeting(b):
    print(f"greeting is executed")
    return f"Hi {b}"


# CALL - execute -argument
result1 = greet('Aven')
print("result1:", result1)

result2 = greeting("Nolin")
print("result2:", result2)


print("=========Keyword & default argumets============")

# DEFINE


def give_greet(name, age=29):  # age=29ga shu yerda qiymat berilsa  defult argument
    print("give_greet is executed")
    return f"Hi {name}, you are {age} years old!"


# CALL
result3 = give_greet(name="Nolon", age=27)  # name ,age keyword argument
print("result3:", result3)


result4 = give_greet("Sem")
print("result4:", result4)


print("=========Scope============")
b = 100  # 3

# DEFINE


def calculate(a, b):  # 2
    c = a * b  # 1
    print(f"the c velue: {c}")


# CALL
calculate(5, 50)
