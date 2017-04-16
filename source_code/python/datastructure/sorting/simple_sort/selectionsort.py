#맨 왼쪽부터 하나씩 최소값을 선택(selection)해 채운다

def SelectionSort(li):
    #최소값을 가지는 인덱스를 담을 인덱스 변수
    minIdx = 0
    #리스트의 길이
    list_len = len(li)
    for i in range(list_len-1):
        #i 전까지는 최소값들로 정렬된 상태
        minIdx = i
        for j in range(i+1, list_len):
            #만약 minIdx의 값이 j보다 크다면 최소값이 아니므로
            #minIdx를 j로 갱신한다
            if li[minIdx] > li[j]:
                minIdx = j
        li[minIdx], li[i] = li[i], li[minIdx]

if __name__ == "__main__":
    li = [4, 6, 1, 7, 2, 8, 3, 5, 9, 10, 12, 11]
    SelectionSort(li)
    print(li)
    
