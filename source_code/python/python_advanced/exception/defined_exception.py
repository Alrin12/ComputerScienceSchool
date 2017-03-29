import sys

class exc1(Exception):
    def __repr__(self):
        return "exc1 error : inherited from Exception"
    #def __str__(self):
    #    return self.__repr__()

class exc2(exc1):
    def __str__(self):
        return "exc2 error : inherited from exc1"

def f1():
    raise exc1("exc1")

def f2():
    raise exc2("exc2")


for f in (f1, f2):
    try:
        f()
    #except:
    #    print(sys.exc_info())
    except (exc1, exc2) as e:
        print(e)

    
