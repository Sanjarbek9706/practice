''' Packages & Debugging
    (1) Python Packages & Core Package
    (2) Package Manager & External Pakage
    (3) Debagging 
'''

import turtle
print("======= Python Packages & Core Package ========")
''' Python  packages/Modules: Core file and External'''
# Core packages  https://docs.python.org/3/library/


# Core package
# t = turtle.Turtle()
# t.shape("turtle")
# t.speed(3)
# t.circle(200)
# turtle.done()

print("--------")
my_file = open("material/message.txt", "r")
try:
    content = my_file.read()
    print("content:", content)
finally:
    my_file.close()

# with - Context manager
with open("material/message.txt", "r") as your_file:
    your_content = your_file.read()
    print("your_content:", your_content)

print("DONE")
