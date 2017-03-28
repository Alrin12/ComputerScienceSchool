# multithreading 
## threading module
---

# GIL
## Global Interpreter Lock
- 파이썬 스레드는 하나의 코어에서만 실행
---

# threading module
```python
import threading
```
---

# Make a thread - 1st way
```python
def thread_main(*args):
	#do something
    
th = threading.Thread(target = thread_main, args = (1, 2,))
```
---

# Make a thread  - 2nd way
```python
class Mainthread(threading.Thread):
	def __init__(self):
    		threading.Thread.__init__(self)
            	#do something
	def run(self):
    		#do something
    	
```
---

# Lock object
## To prevent Race Condition
```python
lock = threading.Lock()
.....

lock.acquire()
#do something with global variables
lock.release()
```
---

# Mutual Exclusion
```python
#gloval variable
g_cnt = 0

def thread_main():
	lock.acquire()
    	#critical section 
    	g_cnt+=1
        lock.release()
```