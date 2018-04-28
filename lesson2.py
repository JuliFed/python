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

hello("fasdf","sdgfas",1,2,3,4,5)
hello2('1',"sdfsf","sdfsdfg","dfgsdfg")

"""Типы данных в Python  
    bool
    int
    float 
"""