#skończyć!!!

class Animal:
    def __init__(self, name):
        self.name = name

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

class Bird(Animal):
    def __init__(self, name):
        super().__init__(name)

class Fish(Animal):
    def __init__(self, name):
        super().__init__(name)