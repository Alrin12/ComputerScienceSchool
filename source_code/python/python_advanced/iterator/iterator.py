'''
iterator = iter([1, 2, 3, 4, 5])

for i in range(5):
    print(next(iterator))
'''

#또 다시 호출하면
#StopIteration 에러
#next(iterator)
import sys

class Seq:
    def __init__(self, fname):
        self.file = open(fname)

    def __del__(self):
        self.file.close()

    def __iter__(self):
        return self

    def __next__(self):
        line = self.file.readline()
        if not line:
            raise StopIteration

        return line


if __name__ == "__main__":
    s = Seq("test.txt")

    s = iter(s)
    print(s)
    
    while True:
        try:
            print(next(s))
        except StopIteration as e:
            break
