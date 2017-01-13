from functools import wraps
from random import randint
from math import sqrt

class DataHandler:  
    def __init__(self):
        self.scores = []
        self.average = []
        self.variance = []
        self.std_dev = []
            
    def checkscores(org_func):
        @wraps(org_func)
        def wrapper(*args, **kwargs):
            print("checkscores_wrapper")
            other = args[0]
            if not other.scores:
                for i in range(0, 10):
                    other.scores.append(randint(0, 100))
            return org_func(*args, **kwargs)
        return wrapper
        
    def checkaverage(org_func):
        @wraps(org_func)
        def wrapper(*args, **kwargs):
            print("checkaverage_wrapper")
            other = args[0]
            if not other.average:
                sum = 0
                for score in other.scores:
                    sum += score
                avg = sum//len(other.scores)
                other.average.append(avg)
            
            return org_func(*args, **kwargs)
        return wrapper

    def checkvariance(org_func):
        @wraps(org_func)
        def wrapper(*args, **kwargs):
            print("checkvariance_wrapper")
            other = args[0]
            if not other.variance:
                sum = 0
                for score in other.scores:
                    a = score - other.average[0]
                    sum += a**2
                vrnc = sum//len(other.scores)
                other.variance.append(vrnc)
            
            return org_func(*args, **kwargs)
        return wrapper


    def GetScores(self):
        print("GetScores")
        if not self.scores:
            for i in range(0, 10):
                self.scores.append(randint(0, 100))
        else:
            pass
    
    @checkscores
    def GetAverage(self):
        print("GetAverage")
        if not self.average:
                sum = 0
                for score in self.scores:
                    sum += score
                avg = sum//len(self.scores)
                self.average.append(avg)
        else:
            pass

    @checkscores
    @checkaverage
    def GetVariance(self):
        print("GetVariance")
        if not self.variance:
                sum = 0
                for score in self.scores:
                    a = score - self.average[0]
                    sum += a**2
                vrnc = sum//len(self.scores)
                self.variance.append(vrnc)
        else:
            pass

    @checkscores
    @checkaverage
    @checkvariance
    def GetStandardDeviation(self):
        print("GetStandardDeviation")
        if not self.std_dev:
            res = sqrt(self.variance[0])
            self.std_dev.append(res)
        else:
            pass


       

if __name__=="__main__":
    dh = DataHandler()
    
    #dh.GetVariance()
    dh.GetStandardDeviation()
    print(dh.scores)
    print(dh.average[0])
    print(dh.variance[0])
    print(dh.std_dev[0])

    dh.GetAverage()
    print(dh.scores)
    print(dh.average[0])

    

    
    

    
    
    
