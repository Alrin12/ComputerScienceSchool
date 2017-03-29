class Stack(list):
    #def push(self, data):
    #    self.append(data)
    push = list.append


if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)

    for i in range(5):
        print(s.pop())


