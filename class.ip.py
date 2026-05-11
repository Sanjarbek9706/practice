'''  CLASS deep diving
    (1) ECABSULATION
    (2) INHERITENCE <
    (3) POLIMORHISM <
'''

print("============ INHERITENCE ==============")
# PARENT > CHILD [only public & protect properties]
# Parent only public & protected properties (state + method) to  children!


class Animal():  # Parent
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

    def make_voice(self):
        print(f"the {self.name} says {self.sound}")


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


print("============ POLIMORHISM ==============")

dog.make_voice()
fish.make_voice()


print("------------------")
# fish > Fish >  Animal > object
a = isinstance(fish, Fish)
b = isinstance(fish, Animal)
c = isinstance(fish, object)
d = isinstance("MIT", object)
result = a and b and c and d
print(f"the reault: {result}")


# Fish > Animal > object
data1 = issubclass(Fish, Animal)
data2 = issubclass(Animal, object)
print("data:", data1, data2)
