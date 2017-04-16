def partition(data, start, end):
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
    data = [2, 5, 4, 1, 8, 10, 5, 3, 6, 6, 5, 7, 9, 12, 11]

    quick_sort(data, 0, len(data) - 1)

    print(data)
    
