def mean_func(n):
    ls_avg = []
    ls_SMA = []
    avg = 0
    SMA = 0
    try:
        while True:
            data = (yield avg, SMA)
            ls_avg.append(data)
            avg = round(sum(ls_avg)/len(ls_avg), 2)

            if len(ls_SMA) >= n:
                ls_SMA.pop(0)
                
            ls_SMA.append(data)
            SMA = round(sum(ls_SMA)/len(ls_SMA), 2)
            
    except GeneratorExit:
        print("coroutine of mean_func closed")
    finally:
        print("good bye")

def printer():
    average = 0
    SMA = 0

    try:
        while True:
            average, SMA = (yield)
            print("average : {}".format(average), end = '     ')
            print("SMA : {}".format(SMA), end = '     ')
            
            print("\n")
            
    except GeneratorExit:
        print("coroutine of printer closed")
    finally:
        print("good bye")
        
class meanhandler:
    def __init__(self, n):
        self.meanfunc = mean_func(n)
        self.printer = printer()
        
        self.average = 0
        self.SMA = 0

        #coroutine 실행 
        next(self.meanfunc)
        next(self.printer)
        
        self.bcalculated = False
        
    def __del__(self):
        self.meanfunc.close()
        self.printer.close()

    def sendData(self, data):
        self.average, self.SMA = self.meanfunc.send(data)      
        
    def dumpData(self, li):
        self.bcalculated = True
        
        for data in li:
            self.sendData(data)
            self.printer.send((self.average, self.SMA))

    def get_SMA(self):
        if self.bcalculated:
            return self.SMA
        else:
            print("Not calculated yet!\nCalculate!!")

    def get_avrg(self):
        if self.bcalculated:
            return self.average
        else:
            print("Not calculated yet!\nCalculate!!")

    def get_result(self):
        print('*' * 30 + "result report" + "*" * 30)
        print("average : {}\nSMA : {}".format(self.average, self.SMA))
        print("*"*73)
        
    
if __name__ == "__main__":
    n = int(input("the number as a denominator for Simple Moving Average : "))
    li = [k for k in range(101) if k % 2 == 0]
    mh = meanhandler(n)
    mh.dumpData(li)
    mh.get_result()
    
    del mh

