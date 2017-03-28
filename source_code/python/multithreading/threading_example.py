import threading, time
from functools import reduce

g_result = 0

# 1st way
'''
def mythread(*arg):
    print("{}    {}    ".format(arg[0], arg[2499]))

    global g_result
    result = reduce(lambda a, b: a + b, arg)

    lock.acquire()
    g_result +=result
    lock.release()
'''

# 2nd way

class mythread(threading.Thread):
    def __init__(self, i_obj):
        threading.Thread.__init__(self)
        self.arr = i_obj
        print("{}    {}    ".format(i_obj[0], i_obj[2499]))
        
    def run(self):
        global g_result
        result = reduce(lambda a, b: a + b, self.arr)
        lock.acquire()
        g_result +=result
        lock.release()





        
lock = threading.Lock()

n = 10000
offset = n//4
li = [k for k in range(n+1)]
threads = []





# 1st way
'''
for i in range(4):
    th = threading.Thread(target = mythread, args =\
                          li[offset *i + 1 : offset*(i+1)+1])
    th.start()
    threads.append(th)
'''

# 2nd way

for i in range(4):
    th = mythread(li[offset * i +1 : offset * (i+1) + 1])
    th.start()
    threads.append(th)






for th in threads:
    th.join()

print("the sum of {num} is {result}".format(result = g_result, num = n))






    
