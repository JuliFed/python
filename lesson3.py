"""Module for lesson 3 """


class Animal:
    """Base Class for animals
    May says ))
    """
    def __init__(self, name):
        self.name = name

    def say(self):
        raise NotImplementedError

    def meal(self):
        print("This is Animal", self.name)

    def __str__(self):
        return "Error: %s" % self.name


class PredatorMixin:
    """Class for cats
    May says and have colors ))
    """
    def meal(self):
        print("This is PredatorMixin", "=", self.name)


class AnimalError(Exception):
    """Class for cats
    May says and have colors ))
    """
    def __init__(self, animal):
        super().__init__()
        self.animal = animal

    def __str__(self):
        return "Error1: %s" % self.animal


# декоратор
def butter(fn):
    def wrapper(self, msg="Rrrrrrr"):
        print("Say", msg)
        fn(self)

    return wrapper


class Cat(PredatorMixin, Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    # @butter
    def say(self, msg):
        if msg == "":
            raise AnimalError(self)
        print(self.name, "says", msg)


# print(Cat.mro())
cat1 = Cat("Leona", "orange")
cat2 = Cat("Barsik", "black")
cat3 = Cat("Murcik", "white")

# cat1.say("")
# cat2.say("ffff")
# test = cat1.say
# test()
# cat1.name = "fdfdfdf"
# test()

# print(cat1.color)
try:
    cat1.say("")
except AnimalError as e:
    print(str(e))
except ValueError as e:
    pass
except SyntaxError as e:
    pass
finally:
    pass
