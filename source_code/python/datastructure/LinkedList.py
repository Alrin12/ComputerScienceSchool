class Node:
    def __init__(self, data, _next = None):
        self.data = data
        self.next = _next

class LinkedList:
    def __init__(self):
        #더미를 가리킨다
        self.head = None
        #마지막 데이터를 가리킨다
        self.tail = None

        #현재 가리키고 있는 노드
        self.current = None
        #current 전을 가리키고 있다
        #delete()함수 호출 시 매우 유용하게 쓰임
        self.before = None

        #데이터의 개수
        self.numOfData =0

        #더미 생성(더미의 역할은 delete나 search시 분기 없이 일괄처리가 가능하기 때문
        dummy = Node("dummy")
        #head와 tail이 더미를 가리키도록 한다.
        self.head = dummy
        self.tail = dummy

    def add(self, data):
        newNode = Node(data)
        self.tail.next = newNode
        self.tail = newNode
        self.numOfData+=1


    #search를 first와 next로 나눈 이유
    #사용자가 지울 데이터를 찾아 지운 후 처음부터 다시 돌아가 search를 할지
    #지운 데이터 이후부터 다시 search를 시작해 다른 데이터를 찾을지
    #원하는 대로 search를 진행할 수 있다
    #만약 find나 search 함수 하나에 순회 기능을 담으면
    #무조건 처음부터 검색해야하는 상태가 된다
        
    #처음부터 search를 시작함
    def first(self):
        self.before = self.head
        self.current = self.head.next

        if self.current:
            return self.current.data, True

        return 0, False

    #current 다음부터 search를 시작한다
    #next()함수를 호출해 True를 반환했다면 이미 current의 값을 반환한 상태
    #다음 번 next()함수를 호출할 때에는 current는 현재 위치의 다음 값을 반환하게 된다!!!
    def next(self):
        if not self.current.next:
            return 0, False

        self.before = self.current
        #current는 현재의 값을 반환하는 게 아니라
        self.current = self.current.next
        #한 노드 이동 후 그 값을 반환한다 : before가 존재하는 이유!
        return self.current.data, True

    #current가 가리키는 값을 지운다
    def delete(self):
        retData = self.current.data
        #refcount가 0이 되면서 garbage collector에 의해 사라진다
        self.before.next = self.current.next
        self.current = self.before
        self.numOfData-=1

        return retData

if __name__ == "__main__":
    lis = LinkedList()
    lis.add(2)
    lis.add(3)
    lis.add(1)
    lis.add(5)
    lis.add(10)
    lis.add(7)
    lis.add(2)

    print("데이터의 개수 : {}".format(lis.numOfData))
    
    data, b_ret = lis.first()
    
    if b_ret:
        print(data, "      ")
        data, b_ret = lis.next()
        while b_ret:
            print(data, "     ")
            data, b_ret = lis.next()

    print("\n")
    
    data, b_ret = lis.first()

    if b_ret:
        if data == 2:
            lis.delete()

        data, b_ret = lis.next()
        while b_ret:
            if data == 2:
                lis.delete()
            data, b_ret = lis.next()

    
    print("데이터의 개수 : {}".format(lis.numOfData))
    data, b_ret = lis.first()
    
    if b_ret:
        print(data, "      ")
        data, b_ret = lis.next()
        while b_ret:
            print(data, "     ")
            data, b_ret = lis.next()

        print("\n")
    





        
