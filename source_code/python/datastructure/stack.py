class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        #LIFO(Last Input First Out)이므로 맨 앞만 가리키고 있으면 됩니다
        self.head = None

    def IsEmpty(self):
        if self.head == None:
            return True

        return False

    def push(self, data):
        newNode = Node(data)

        newNode.next = self.head
        self.head = newNode

    def pop(self):
        if self.head == None:
            print("There is no data")
            exit(-1)

        retData = self.head.data

        self.head = self.head.next
        return retData

    def peek(self):
        if self.head == None:
            print("There is no data")
            exit(-1)

        return self.head.data

if __name__ == "__main__":
    stack = Stack()

    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)

    while not stack.IsEmpty():
        print(stack.pop())

        
