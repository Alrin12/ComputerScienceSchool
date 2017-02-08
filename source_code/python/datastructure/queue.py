class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def IsEmpty(self):
        if not self.head:
            return True

        return False

    def Enqueue(self, data):
        newNode = Node(data)
        
        if not self.head:
            self.head = newNode
            self.tail = newNode
            return

        self.tail.next = newNode
        self.tail = newNode

    def Dequeue(self):
        if not self.head:
            print("There is no data")
            exit(-1)

        retData = self.head.data
        self.head = self.head.next

        return retData

    def Peek(self):
        if not self.head:
            print("There is no data")
            exit(-1)

        return self.head.data

if __name__ == "__main__":
    queue = Queue()

    queue.Enqueue(1)
    queue.Enqueue(2)
    queue.Enqueue(3)
    queue.Enqueue(4)
    queue.Enqueue(5)

    while not queue.IsEmpty():
        print(queue.Dequeue())


    
