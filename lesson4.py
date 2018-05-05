class Foo:
    def __init__(self):
        self.i = 0
        self.x = [1, 2, 3]

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return self.x[self.i]
        except IndexError:
            raise StopIteration
        finally:
            self.i = self.i + 1


y = Foo()
for i in y:
    print(i)

for i in y:
    print(i)
