#이미 정렬되어 있는 배열에 데이터를 삽입(insertion)한다고 하여 InsertionSort
def InsertionSort(li):
    list_length = len(li)

    for i in range(1, list_length):
        unsortedData = li[i]
        properIdx = 0

        for j in range(i-1, -1, -1):
            if li[j] > unsortedData:
                li[j+1] = li[j]
            else:
                properIdx = j+1
                break
            
        li[properIdx] = unsortedData

if __name__ == "__main__":
    li = [2, 5, 7, 3, 6, 1, 4, 8]
    InsertionSort(li)
    print(li)
    

            





    
