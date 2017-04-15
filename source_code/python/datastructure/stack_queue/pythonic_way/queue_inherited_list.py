class Queue(list):
    enqueue = list.append
    def dequeue(self):
        return self.pop(0)

if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)

    for i in range(5):
        print(q.dequeue())
