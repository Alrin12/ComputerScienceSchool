class Queue(list):
    enqueue = list.append

    def dequeue(self):
        return self.pop(0)

    def peek(self):
        return self[0]

    def size(self):
        return len(self)

if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)

    for i in range(q.size()):
        print("peek of queue : {}".format(q.peek()))
        print(q.dequeue())

