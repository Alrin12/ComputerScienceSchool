#pragma once
#include "Heap.h"

template<typename T, int size>
class PriorityQueue
{
private:
	Heap<T, size> * heap;
public:
	PriorityQueue(const char * s_min_max)
	{
		heap = new Heap<T, size>(s_min_max);
	}
	~PriorityQueue()
	{
		delete heap;
	}
	bool IsEmpty()
	{
		return heap->IsEmpty();
	}

	int GetNumOfData()
	{
		return heap->GetNumOfData();
	}

	void Enqueue(T data)
	{
		heap->Insert(data);
	}
	T Dequeue()
	{
		return heap->Delete();
	}
};
