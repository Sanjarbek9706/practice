'''  CLASS deep diving
    (1) ECABSULATION
    (2) INHERITENCE <
    (3) POLIMORHISM <
'''

print("============ INHERITENCE ==============")
# PARENT > CHILD


class Animal:  # Parent
    # state
    description = "The class is parent for animal"

    # constructor
    def __init__(self, voice):
        self.status = "animal is alive"
        self.voice = voice

    # method
    def make_voice(self):
        print(f"the animal can  make voice: {self.voice}")


class Dog(Animal):  # child
    # state

    # constuctor
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    # method
    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def protect(self):
        print("Yes I can protect you!")


class Cat(Animal):  # child
    # state

    # constuctor
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    # method
    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def play(self):
        pass


class Fish(Animal):  # child

    # state

    # constuctor
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    # method
    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def swim(self):
        print("Yes I can swim!")


dog = Dog("Rex", "wofw", True)
cat = Cat("Tom", "myeow", True)
fish = Fish("Nemo", "Zzz", False)

dog.introduce()
cat.introduce()
fish.introduce()

print("------------------")
dog.make_voice()
fish.make_voice()

print("--------------")
print(Animal.description)
print(Dog.description)

print(dog.voice, fish.voice)
print("dog.status:", dog.status)
print("cat.status:", cat.status)
print("fish.status:", fish.status)
