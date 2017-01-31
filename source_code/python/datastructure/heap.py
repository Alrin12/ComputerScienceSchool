class Heap:
    #부모 노드를 구하는 함수
    def GetParentIdx(self, idx):
        return idx//2

    #왼쪽 자식 노드를 구하는 함수
    def GetLeftChildIdx(self, idx):
        return idx * 2

    #오른쪽 자식 노드를 구하는 함수
    def GetRightChildIdx(self, idx):
        return idx * 2 + 1

    def __init__(self, arr_length = 100, s_min_max = "min"):
        #dynamic array의 역할을 리스트가 한다
        self.dynamicArr = [ None  for i in range(arr_length+1)]
        #맨 마지막 노드의 index와 일치한다
        self.numOfData = 0
        #최소 힙 아니면 최대 힙을 나타내는 flag 역할
        #1 : min heap(최소 힙), 2 : max heap(쵀대 힙)
        if s_min_max == "min":
            self.min_max = 1
        elif s_min_max == "max":
            self.min_max = 2
        else:
            self.min_max = 1

    def IsEmpty(self):
        if self.numOfData == 0:
            return True
        else:
            return False

    def GetNumOfData(self):
        return self.numOfData
    
    #Insert()함수에서 부모 노드와 비교
    #부모 노드 값과 바꿔야 하는지 판단하는 함수
    def IsGoUp(self, idx, data):
        #idx가 루트 노드라면 그만 올라가라!
        if idx <=1:
            return False
        
        #부모 노드에 저장된 값을 받아와서
        value = self.dynamicArr[self.GetParentIdx(idx)]

        #최소 힙이면 1
        if self.min_max == 1:
            #데이터가 부모 노드 값보다 작으면 올라가!
            if value > data:
                return True
            else:
                return False
        #최대 힙이면 2
        elif self.min_max == 2:
            #데이터가 부모 노드 값보다 크면 올라가!
            if value < data:
                return True
            else:
                return False
        
    def Insert(self, data):
        #만약 heap이 비어있다면
        if self.IsEmpty():
            self.numOfData +=1
            self.dynamicArr[self.numOfData] = data
            return
        #새로운 노드가 생겼으므로 numOfData는 1 상승
        self.numOfData+=1
        #데이터의 인덱스에 맨마지막 인덱스 값(numOfData)를 받아온 후
        idx_data = self.numOfData

        #부모 노드 값과 비교해 바꿀지 말지를 계속 수행하여
        #heap에서 알맞은 위치에
        #(최소 힙이면 부모보다 크면 더 이상 바꿀 필요 없다)
        while self.IsGoUp(idx_data, data):
            #부모 노드의 값을 자식 노드로 이동시키고
            self.dynamicArr[idx_data] = self.dynamicArr[self.GetParentIdx(idx_data)]
            #성능을 고려하여 최종 위치를 정하기 전에는
            #실제로 데이터를 리스트에 저장하지는 않고
            #인덱스 값만 부모 노드로 바꾸어 준다
            idx_data = self.GetParentIdx(idx_data)
            
        #최종 위치가 정해지면 그때 리스트에 데이터를 입력한다
        self.dynamicArr[idx_data] = data


    #Delete()를 구현하는 데 필요한 함수목록 1 : WhichIsPriorChild()
    #두 자식 노드를 비교해 우선 순위가 높은 자식 노드를 반환
    def WhichIsPriorChild(self, idx):
        #왼쪽 자식 노드의 인덱스를 구해서
        left_idx = self.GetLeftChildIdx(idx)

        #만약 맨 마지막 노드 인덱스 보다 크다면 단말 노드
        #자식 노드가 없다는 의미로 -1을 반환하기로 한다
        #IsGoDown()함수에서 반환값 -1을 처리하기로 한다
        if left_idx > self.numOfData:
            return -1
        
        #만약 맨 마지막 노드 인덱스라면 왼쪽 자식 노드만 있는 상황
        #그렇다면 두 자식 노드를 비교할 필요 없이 왼쪽 자식 노드를 반환
        elif left_idx == self.numOfData:
            return left_idx
        
        #왼쪽 자식 노드 값
        left_value = self.dynamicArr[self.GetLeftChildIdx(idx)]
        #오른쪽 자식 노드 값
        right_value = self.dynamicArr[self.GetRightChildIdx(idx)]

        #최소 힙이라면
        if self.min_max == 1:
            #두 자식 노드 값을 비교하여 작은 값을 가진 자식 노드의 인덱스를 반환
            if left_value < right_value:
                return self.GetLeftChildIdx(idx)
            else:
                return self.GetRightChildIdx(idx)
        #최대 힙이라면
        elif self.min_max == 2:
            #두 자식 노드 값을 비교하여 큰 값을 가진 자식 노드의 인덱스를 반환
            if left_value > right_value:
                return self.GetLeftChildIdx(idx)
            else:
                return self.GetRightChildIdx(idx)

    #Delete()를 구현하는 데 필요한 함수목록 2 : IsGoDown()
    #자식 노드 값과 바꿔야 하는지를 판단하는 함수
    def IsGoDown(self, idx, data):
        child_idx = self.WhichIsPriorChild(idx)

        #만약 반환받은 자식 노드 인덱스가 -1이면 자식 노드가 없다는 의미이므로
        if child_idx < 0:
            return False

        #우선 순위가 높은 자식 노드의 값을 받아온다
        value = self.dynamicArr[child_idx]

        #최소 힙이라면
        if self.min_max == 1:
            #데이터가 자식노드 값 보다 크면 바꿔야 한다
            if value < data:
                return True
            else:
                return False
        #최대 힙이라면
        elif self.min_max == 2:
            #데이터가 자식 노드 값 보다 작으면 바꿔야 한다
            if value > data:
                return True
            else:
                return False
            
    def Delete(self):
        if self.IsEmpty():
            print("There is no data")
            exit(-1)
        elif self.numOfData == 1:
            self.numOfData-=1
            return self.dynamicArr[1]
        retData = self.dynamicArr[1]
        lastData = self.dynamicArr[self.numOfData]
        self.numOfData-=1

        idx_data = 1

        while self.IsGoDown(idx_data, lastData):
            self.dynamicArr[idx_data] = self.dynamicArr[self.WhichIsPriorChild(idx_data)]
            idx_data = self.WhichIsPriorChild(idx_data)

        self.dynamicArr[idx_data] = lastData
        return retData
            

if __name__ == "__main__":
    heap = Heap(100, "min")
    heap.Insert(3)
    heap.Insert(5)
    heap.Insert(1)
    heap.Insert(10)
    heap.Insert(8)
    heap.Insert(7)
    heap.Insert(4)
    heap.Insert(5)
    heap.Insert(2)
    heap.Insert(6)
    heap.Insert(9)

    ndata = heap.GetNumOfData()
    
    #insert가 잘 되었는지 테스트 코드
    for i in range(1, ndata+1):
        print(heap.dynamicArr[i])

    print("\n\n")

    #delete가 잘 되었는지 테스트
    
    for i in range(1, ndata+1):
        print(heap.Delete())
    
    

        

        
        
