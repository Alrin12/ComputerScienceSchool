
call_of_partition = 0

def get_pivot(data, start, end):
    mid = (start + end)//2
    list_idx = [start, mid, end]

    #bubble sort
    if data[list_idx[0]] > data[list_idx[1]]:
        list_idx[0], list_idx[1] = list_idx[1], list_idx[0]
    if data[list_idx[1]] > data[list_idx[2]]:
        list_idx[1], list_idx[2] = list_idx[2], list_idx[1]
    if data[list_idx[0]] > data[list_idx[1]]:
        list_idx[0], list_idx[1] = list_idx[1], list_idx[0]

    return list_idx[1]

def partition(data, start, end):
    global call_of_partition
    call_of_partition += 1

    idx_pivot = get_pivot(data, start, end)
    data[start], data[idx_pivot] = data[idx_pivot], \
                                   data[start]

    pivot = data[start]

    low = start + 1
    high = end

    #교차하기 전까지
    while low <=high:
        while low <=end and data[low] <= pivot:
            low += 1

        while high >=(start + 1) and data[high] >= pivot:
            high -= 1

        if low <= high:
            data[low], data[high] = data[high], data[low]

    data[start], data[high] = data[high], data[start]

    return high

def quick_sort(data, start, end):
    #탈출조건
    if start >= end:
        return

    idx_pivot = partition(data, start, end)

    quick_sort(data, start, idx_pivot - 1)
    quick_sort(data, idx_pivot + 1, end)

if __name__ == "__main__":
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

    quick_sort(data, 0, len(data) - 1)

    print(data)
    print("call_of_partition : {}".format(call_of_partition))
    
