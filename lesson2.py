#Comment
def hello(*names,**kwargs):
    for name in names:
        print(name)

def hello2(*names):
    it = iter(names)
    while True:
        try:
            x = next(it)
            print("Hello "+x)
        except StopIteration:
            return

"""Comment
    many
        strings"""

#hello("fasdf","sdgfas",1,2,3,4,5)
#hello2('1',"sdfsf","sdfsdfg","dfgsdfg")

"""Типы данных в Python  
    bool, int, float
    
    list, tuple 
"""

# list,tuple
x = 123
y = ["sss","aaa","qqqq"]
z = ("a","b","c")

print(x,id(x))
print(y,id(y))
print(z,id(z))
print()
x += 5
y += [5]
z += (5,)
print(x,id(x))
print(y,id(y))
print(z,id(z))


# значения передаются по ссылке
print()
x = 123
def foo(x):
    print(id(x))

print(id(x))
foo(x)