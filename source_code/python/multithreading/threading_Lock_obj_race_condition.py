import threading, time

g_count = 0

def thread_main():
    global g_count
    lock.acquire()
    for i in range(1000000):
        g_count+=1
    lock.release()

lock = threading.Lock()

threads = []


for i in range(50):
    th = threading.Thread(target = thread_main)
    th.start()
    threads.append(th)

for th in threads:
    th.join()

print("g_count : {:,}".format(g_count))
