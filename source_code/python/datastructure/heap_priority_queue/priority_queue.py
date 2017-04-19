from heap import Heap

class PriorityQueue(Heap):
    enqueue = Heap.insert
    dequeue = Heap.delete

if __name__ == "__main__":
    pq = PriorityQueue("min")
    pq.enqueue(3)
    pq.enqueue(7)
    pq.enqueue(2)
    pq.enqueue(1)
    pq.enqueue(9)
    pq.enqueue(5)
    pq.enqueue(8)
    pq.enqueue(10)
    pq.enqueue(5)
    pq.enqueue(6)
    pq.enqueue(4)

    for i in range(1, pq.size()+1):
        print(pq.dynamic_arr[i], end = '  ')

    print("\n")

    for i in range(1, pq.size()+1):
        print(pq.dequeue(), end = '  ')
