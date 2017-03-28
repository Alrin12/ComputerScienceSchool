import threading, random, time
import queue

class Producer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.data =["math", "physics", "literature", "physical education"]
        self.timer = 3
        self.elapsed_time = 0
        
    def run(self):
        global q
        
        t1 = time.time()
        cnt = 0
        
        while cnt < 10:
            self.elapsed_time = time.time() - t1
            if self.elapsed_time > self.timer:
                q.put(self.data[random.randrange(len(self.data))])
                self.elapsed_time = 0
                t1 = time.time()
                cnt+=1
                
class Consumer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.data = []
        self.timer = 5
        self.elapsed_time = 0

    def run(self):
        global q

        t1 = time.time()
        cnt = 0
        
        while cnt < 10:
            self.elapsed_time = time.time() - t1
            if self.elapsed_time > self.timer:
                self.data.append(q.get())
                print("consumer gets data of {}".format(self.data[-1]))
                self.elapsed_time = 0
                t1 = time.time()
                cnt+=1

q = queue.Queue()
NUM_OF_PRODUCERS = 3
NUM_OF_CONSUMERS = 3

producers = []
consumers = []

for i in range(NUM_OF_PRODUCERS):
    producers.append(Producer())

for i in range(NUM_OF_CONSUMERS):
    consumers.append(Consumer())

for i in range(NUM_OF_PRODUCERS):
    producers[i].start()

for i in range(NUM_OF_CONSUMERS):
    consumers[i].start()

for i in range(NUM_OF_CONSUMERS):
    producers[i].join()

for i in range(NUM_OF_CONSUMERS):
    consumers[i].join()

print("done")
            
        
