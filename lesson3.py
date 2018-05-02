class Animal:

    def __init__(self, name):
        self.name = name

    def say(self):
        raise NotImplementedError

    def meal(self):
        print("Animal")


class PredatorMixin:
    def meal(self):
        print("This is PredatorMixin")


class Cat(Animal, PredatorMixin):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def say(self):
        print("meow")


my_cat = Cat("Leon", "red")
my_cat.meal()
my_cat.say()
print(my_cat.color)




