from collections import namedtuple

# import argparse
#
# parser = argparse.ArgumentParser(description='Process some integers.')
# parser.add_argument('--field_size', '-f', metavar='-f', type=int, help='Size of game field')
# args = parser.parse_args()
# print('Field size =', args.field_size)

#
# class Bar:
#     _x = 0
#
#     @property
#     def foo(self):
#         return self._x
#
#     @foo.setter
#     def foo(self, value):
#         self._x = value ** 2
#
#     @foo.deleter
#     def foo(self):
#         del self._x
#
#
# print('Bar')
# bar = Bar()
# print(bar.foo)
# bar.foo = 2
# print(bar.foo)
# del bar.foo
# print(bar.foo)
#
#
# class Property:
#     def __init__(self, getter, setter, deleter):
#         self.g = getter
#         self.s = setter
#         self.d = deleter
#
#     def __get__(self, obj, cls=None):
#         if self.g is None:
#             raise AttributeError
#         return self.g(obj)
#
#     def __set__(self, obj, value):
#         if self.s is None:
#             raise AttributeError
#         self.s(obj, value)
#
#     def __delete__(self, obj):
#         if self.d is None:
#             raise AttributeError
#         self.d(obj)
#
#
# class Bar2:
#     _x = None
#
#     def getx(self):
#         return self._x
#
#     def setx(self, value):
#         self._x = value ** 2
#
#     def delx (self):
#         del self._x
#
#     foo = Property(getx, setx, delx)
#
#
# print('Bar2 with Property')
# bar2 = Bar2()
# print(bar2.foo)
# bar2.foo = 25
# print(bar2.foo)
# del bar2.foo
# print(bar2.foo)
#
#
# # @staticmethod под капотом
# class StaticMethod:
#     def __init__(self, f):
#         self.f = f
#
#     def __get__(self, obj, cls="None"):
#         return self.f
#
#
# class ClassMethod:
#     def __init__(self, f):
#         self.f = f
#
#     # def __get__(self, obj, cls="None"):
#     #     return self.f
#
#     def __get__(self, obj, cls="None"):
#         def wrapper(*args, **kwargs):
#             return self.f(cls, *args, **kwargs)
#         return wrapper()
#
#
# class BoundMethod:
#     def __init__(self, f):
#         self.f = f
#
#     def __get__(self, obj, cls="None"):
#         def wrapper(*args, **kwargs):
#             return self.f(obj, *args, **kwargs)  # вместо класса прокидываем obj в отличие от static
#         return wrapper()
#
#
# class Square(int):
#     def __new__(cls, n):
#         return super().__new__(cls, n ** 2)
#
#
# print('Square')
# sq = Square(7)
# print(sq)

# Person = namedtuple('Person', ['name', 'age'])
#
#
# class Person(Person):
#     def __new__(cls, *args, **kwargs):
#         kwargs['name'] = kwargs['name'].title()
#         return super().__new__(cls, *args, **kwargs)
#
#
# p = Person(name='vasYa', age=20)
# print(p.name)


# Метаклассы
class Person(Person):
    def __new__(cls, *args, **kwargs):
        kwargs['name'] = kwargs['name'].title()
        return super().__new__(cls, *args, **kwargs)


p = Person(name='vasYa', age=20)
print(p.name)
