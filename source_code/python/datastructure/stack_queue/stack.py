class Stack(list):
    push = list.append

    def peek(self):
        return self[-1]

    def size(self):
        return len(self)

if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)

    for i in range(s.size()):
        print("peek of stack : {}".format(s.peek()))
        print(s.pop())

    
