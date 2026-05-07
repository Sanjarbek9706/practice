''' FUNCTIONLAR > DARS REJASI:
1) Functionlarning Define va Call jarayoni
2) Parametr va Argument
3) Keyword va Default argumentlar
4)Functionlarda Scope tushunchasini organamiz
'''
print("=========DEFINE vs CALL============")
# build in function > print() type()
# Function - reusable block of code!
# Instead of block {} in JAVA, Python use indentation!


# DEFINE - build
def greet(a):  # void function qiymat qaytarmaydi
    print(f"How do you do, {a}")


# return functiom qiymat qaytaradi
def greeting(b):
    print(f"greeting is executed")
    return f"Hi {b}"


# CALL - execute
result1 = greet('Aven')
print("result1:", result1)

result2 = greeting("Nolin")
print("result2:", result2)
