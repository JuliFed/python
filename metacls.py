class TypeCheck:
    def __init__(self, cls):
        self.name = None
        self.attr = None
        self.type = cls

    def __get__(self, obj, cls):
        if obj is None:
            return self

        return getattr(obj, self.attr)

    def __set__(self, obj, value):
        if not isinstance(value, self.type):
            raise TypeError('%s must be of type(s) %s (got %r)' % (
                self.name,
                self.type,
                value,
            ))
        else:
            setattr(obj, self.attr, value)


class Typed(type):
    # https://stackoverflow.com/a/35730545
    # __instancecheck__(self, instance)
    # __subclasscheck__(self, subclass)

    def __new__(mcls, name, bases, namespace, **kwargs):
        for attr, value in namespace.items():
            if isinstance(value, TypeCheck):
                value.name = name
                value.attr = '_' + name

        return super().__new__(mcls, name, bases, namespace, **kwargs)


class Person(metaclass=Typed):
    age = TypeCheck(int)
    name = TypeCheck(str)


def main():
    person = Person()
    person.age = 20
    person.name = "vasya"

    try:
        person.age = "20"
    except TypeError as e:
        print(str(e))


if __name__ == "__main__":
    main()