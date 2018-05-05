# Comment
def hello(*names, **kwargs):
    for name in names:
        print(name)


def hello2(*names):
    it = iter(names)
    while True:
        try:
            x = next(it)
            print("Hello " + x)
        except StopIteration:
            return


"""Comment
    many
        strings"""
# hello("fasdf","sdgfas",1,2,3,4,5)
# hello2('1',"sdfsf","sdfsdfg","dfgsdfg")

"""Типы данных в Python  
    bool, int, float
    
    list, tuple 
"""

# list,tuple
x = 123
y = ["sss", "aaa", "qqqq"]
z = ("a", "b", "c")

print(x, id(x))
print(y, id(y))
print(z, id(z))
print()
x += 5
y += [5]
z += (5,)
print(x, id(x))
print(y, id(y))
print(z, id(z))

# значения передаются по ссылке
print()
x = 123


def foo(x):
    print(id(x))


print(id(x))
foo(x)

# dict
x = {
    123: 123,
    '123': 124,
    "dddd": "ddd",
}

print(x["123"])
print(x[123])

# string format
print("Hello %s" % "user")
print("Hello %d" % 1022)
print("Hello %02d" % 1)
print("%.2f" % 0.1)

# разобраться с байтами! bytes
# разобраться с utf-8
print(b'fgsdfg'[1])
print("привет".encode('utf-8'))
print("привет".encode('cp1251'))
b = "привет".encode('cp1251')
print(b.decode('cp1251'))

# string, tuple, list, bytes
print("assdffghhjj"[2:5])
print("assdffghhjj"[:3])
print("assdffghhjj"[::2])

w = range(10, 20, 2)
# w = range(10)
for i in w:
    print(i, end=' ')

print(1 in w)

# def foo(a, b, *args, c = b, **kwargs)


def foo(a, b, c="abc"):
    print(a,b,c)


foo(1, 2, 3)
foo(1, 2)


def test(a, g, *, c="x"):
    print(a, g, c)


# test(2, 3, 4)
# test(2, 3)

print("kwd", test.__kwdefaults__)
test.__kwdefaults__["c"] = "zzz"
print("kwd", test.__kwdefaults__)


# Задачки

def fact(n):
    if n == 0:
        return 0
    return n * fact(n-1)


print("Fact 0:", fact(0))
print("Fact 5:", fact(5))


def fib(n):
    result = []
    a, b = 0, 1
    result.append(a)
    result.append(b)
    for i in range(2, n):
        x = a + b
        result.append(x)
        a, b = b, x
    return result


print(fib(5))
print(fib(20))


def fib_gen(n):
    if n <= 1:
        return 0
    yield 0
    yield 1
    a, b = 0, 1
    for i in range(2, n):
        a, b = b, a + b
        yield b


for i in fib_gen(20):
    print(i, end=', ')


