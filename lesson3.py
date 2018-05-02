class Animal:
    def __init__(self, name):
        self.name = name

    def say(self):
        raise NotImplementedError

    def meal(self):
        print("This is Animal")


class PredatorMixin:
    def meal(self):
        print("This is PredatorMixin", "=", self.name)


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

    @butter
    def say(self, msg="meow"):
        print(self.name, "says", msg)


# print(Cat.mro())
cat1 = Cat("Leona", "orange")
cat2 = Cat("Barsik", "black")
cat3 = Cat("Murcik", "white")

cat1.say()
cat2.say("ffff")
test = cat1.say
# test()
# cat1.name = "fdfdfdf"
# test()

# print(cat1.color)

