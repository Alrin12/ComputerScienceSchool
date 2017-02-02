#성능 비교를 위한 변수
call_of_exchange = 0


'''
#정렬된 리스트에서 맨 앞 값을 pivot으로 지정한다면
#예를 들어 1
#성능이 매우 안 좋을 수 있다
#그러므로 pivot 값을 정하는 함수를 따로 만들어
#pivot 값이 가장 작은 값이 되지 않도록 한다
def get_pivot(li, start, end):
    mid = (start + end)//2
    list_idx = [start, mid, end]

    #버블 정렬로 리스트에서의 값을 비교해
    #[가장 작은 값의 index, 가운데 값의 index, 가장 큰 값의 index]
    #순으로 정렬한다
    if li[list_idx[0]] > li[list_idx[1]]:
        list_idx[0], list_idx[1] = list_idx[1], list_idx[0]
    if li[list_idx[1]] > li[list_idx[2]]:
        list_idx[1], list_idx[2] = list_idx[2], list_idx[1]
    if li[list_idx[0]] > li[list_idx[1]]:
        list_idx[0], list_idx[1] = list_idx[1], list_idx[0]

    #정렬이 완료되면 가운데 idx의 값이 중간 값이므로 이를 반환해
    #pivot으로 정하도록 한다
    return list_idx[1]
'''


def exchange(li, start, end):
    #exchange 함수가 몇 번 호출되었는가를 계산
    global call_of_exchange
    call_of_exchange += 1
    
  
    '''
    #pivot 값을 정한다
    idx_pivot = get_pivot(li, start, end)

    #pivot을 리스트의 start index에 두기 위해
    #리스트의 start 값과 pivot idx의 값을 교환한다
    li[start], li[idx_pivot] = li[idx_pivot], li[start]
    '''

    
    #pivot 여기서는 start index의 값을 의미한다
    pivot = li[start]
    #pivot 값을 기준으로 왼쪽에 낮은 값들이 존재할 수 있도록
    #low idx는 검색 도중 pivot보다 큰 값이 있으면
    #그 값을 가리킨다
    low = start + 1
    #pivot 값을 기준으로 오른쪽에 높은 값들이 존재할 수 있도록
    #high idx는 pivot 값보다 작은 값이 있으면
    #그 값을 기리킨다
    high = end

    #반드시 low와 high idx가 교차하게 만든다
    #그 전까지는 교환 규칙에 따라 계속 루프가 돌도록 한다
    while low <= high:
        #low idx는 pivot보다 큰 값을 가진 idx를 만나기 전까지
        #오른쪽으로 이동한다
        #대신 low가 end를 벗어나면 안된다
        while low <= end and li[low] <= pivot:
            low+=1

        #high idx는 pivot보다 작은 값을 가진 idx를 만나기 전까지
        #왼쪽으로 이동한다
        #대신 high가 start + 1을 벗어나면 안된다
        while high >= (start + 1) and li[high] >= pivot:
            high-=1

        #low와 high가 교차 전이라면 두 idx가 가리키는 값을 서로 바꾼다
        if low <= high:
            li[low], li[high] = li[high], li[low]

    #교차했다면 pivot의 idx와 high idx의 값을 서로 교환한다
    #high가 가리키는 idx가 정렬되었을 때의 pivot 값의 위치이기 때문
    li[start], li[high] = li[high], li[start]

    #최종적으로 pivot 값의 최종 idx를 반환
    return high

def quicksort(li, start, end):
    #재귀함수 이므로 탈출 조건이 필요하다
    if start >=end:
        return;

    #정렬된 pivot값의 idx를 가져온다
    idx_pivot = exchange(li, start, end)

    #idx_pivot은 정렬이 된 상태 이므로 이를 기준으로
    #앞 부분과 뒷 부분을 quicksort를 통해(재귀함수) 계속 정렬해주면 된다
    quicksort(li, start, idx_pivot - 1)
    quicksort(li, idx_pivot + 1, end)


if __name__ == "__main__":
    li = [2, 5, 4, 1, 8, 10, 5, 3, 6, 6, 5, 7, 9, 12, 11]

    #정렬된 리스트에서의 성능 평가를 위한 리스트
    #li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    
    quicksort(li, 0, len(li)-1)

    print(li)
    print("call_of_exchange : %d \n" % call_of_exchange)

    

    
            
