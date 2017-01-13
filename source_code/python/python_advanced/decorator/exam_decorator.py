from functools import wraps
from random import randint
from math import sqrt

s = []
a = []
v = []
s_d = []

  
def checkscores(org_func):
    @wraps(org_func)
    def wrapper(*args, **kwargs):
        print("checkscores_wrapper")
        scores=args[0]
        if not scores:
            for i in range(0, 10):
                scores.append(randint(0, 100))
        return org_func(*args, **kwargs)
    return wrapper


'''
@checkscores
def GetAverage(scores, average):
    sum = 0
    for score in scores:
        sum += score
    avg = sum//len(scores)
    average.append(avg)

GetAverage(s, a)
print(s)
print(a)
'''
 

def checkaverage(org_func):
    @wraps(org_func)
    def wrapper(*args, **kwargs):
        print("checkaverage_wrapper")
        scores = args[0]
        average = args[1]
        if not average:
            sum = 0
            for score in scores:
                sum += score
            avg = sum//len(scores)
            average.append(avg)
            
        return org_func(*args, **kwargs)
    return wrapper
'''
@checkscores
@checkaverage
def GetVariance(scores, average, variance):
    sum = 0
    for score in scores:
        a = score - average[0]
        sum += a**2
    vrnc = sum//len(scores)
    variance.append(vrnc)

GetVariance(s, a, v)
print(s)
print(a)
print(v)
'''

def checkvariance(org_func):
    @wraps(org_func)
    def wrapper(*args, **kwargs):
        print("checkvariance_wrapper")
        scores = args[0]
        average = args[1]
        variance = args[2]
        if not variance:
            sum = 0
            for score in scores:
                a = score - average[0]
                sum += a**2
            vrnc = sum//len(scores)
            variance.append(vrnc)
            
        return org_func(*args, **kwargs)
    return wrapper
    
@checkscores
@checkaverage
@checkvariance
def GetStandardDeviation(scores, average, variance, std_dev):
    print("GetStandardDeviation")
    res = sqrt(variance[0])
    std_dev.append(res)

GetStandardDeviation(s, a, v, s_d)

print(s)
print(a)
print(v)
print(s_d)


            
        
        


            
            
                
            
