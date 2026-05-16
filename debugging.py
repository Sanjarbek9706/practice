''' Packages & Debugging
    (1) Python Packages & Core Package
    (2) Package Manager & External Pakage
    (3) Debagging 
'''

from PIL import Image
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

print("======= Package Manager & External Pakage ========")
''' Package Managers
    Python > pip pipenv
    NodeJS > npm yarn
    PHP > composer
    MacOS > brew
 '''
# External package > https://pypi.org/

with Image.open("material/logo.png") as img_obj:
    resize_img = img_obj.resize((200, 200))
    resize_img.show()
    resize_img.save("material/semple.png")
