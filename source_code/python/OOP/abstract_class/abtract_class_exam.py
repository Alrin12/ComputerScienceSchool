from abc import * # abstract base class

class Base(metaclass = ABCMeta):
    @abstractmethod
    def abs_meth(self):
        pass

class Derived(Base):
    def abs_meth(self):
        print("abs_meth must be overridden")

#error
#b = Base()
        
d = Derived()
d.abs_meth()
