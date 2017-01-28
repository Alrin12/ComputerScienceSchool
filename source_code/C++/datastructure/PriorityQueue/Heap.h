#pragma once
#include <iostream>
#include <cstring>
using namespace std;

template <typename T, int size>
class Heap
{
private:
	T dynamicArr[size];
	int numOfData;//can be the last index
	int min_max;//min heap or max heap
	            //1 : min heap(ÃÖ¼Ò Èü), 2: max heap(ÃÖ´ë Èü)
public:
	Heap(const char * s_min_max = "min") : numOfData(0) 
	{
		if (!strcmp(s_min_max, "min"))
			min_max = 1;
		else if (!strcmp(s_min_max, "max"))
			min_max = 2;
		else
			min_max = 1;
	}

	bool IsEmpty();
	
	void Insert(T data);
	T Delete();
	int GetNumOfData()
	{
		return numOfData;
	}
private:
	//functions needed to create Insert() and Delete()
	int GetParentIdx(int idx);
	int GetLeftChildIdx(int idx);
	int GetRightChildIdx(int idx);

	//function needed to create Insert()
	bool IsGoUp(int idx, T data);

	//function needed to create Delete()
	int WhichIsPriorChild(int idx);
	bool IsGoDown(int idx, T data);
};

template<typename T, int size>
bool Heap<T, size>::IsEmpty()
{
	if (numOfData == 0)
		return true;
	else
		return false;
}

template<class T, int size>
void Heap<T, size>::Insert(T data)
{
	if (IsEmpty())
	{
		numOfData++;
		dynamicArr[numOfData] = data;
		return;
	}

	numOfData++;
	int idx_data = numOfData;

	while (IsGoUp(idx_data, data))
	{
		dynamicArr[idx_data] = dynamicArr[GetParentIdx(idx_data)];
		idx_data = GetParentIdx(idx_data);
	}
	dynamicArr[idx_data] = data;
}

template<typename T, int size>
T Heap<T, size>::Delete()
{
	if (IsEmpty())
	{
		cout << "There is no data" << '\n';
		exit(-1);
	}
	else if (numOfData == 1)
	{
		numOfData--;
		return dynamicArr[1];
	}

	T retData = dynamicArr[1];
	T lastData = dynamicArr[numOfData];
	numOfData--;

	int idx_data = 1;

	while (IsGoDown(idx_data, lastData)){
		dynamicArr[idx_data] = dynamicArr[WhichIsPriorChild(idx_data)];
		idx_data = WhichIsPriorChild(idx_data);
	}
	dynamicArr[idx_data] = lastData;
	return retData;
}

template<typename T, int size>
int Heap<T, size>::GetParentIdx(int idx)
{
	return idx >> 1;
}

template<typename T, int size>
int Heap<T, size>::GetLeftChildIdx(int idx)
{
	return idx << 1;
}


template<typename T, int size>
int Heap<T, size>::GetRightChildIdx(int idx)
{
	return (idx << 1) + 1;
}

template<class T, int size>
bool Heap<T, size>::IsGoUp(int idx, T data)
{
	if (idx <= 1)
		return false;

	T value = dynamicArr[GetParentIdx(idx)];
	switch (min_max)
	{
	case 1://min heap
		if (value > data)
			return true;
		else
			return false;
	case 2://max heap
		if (value < data)
			return true;
		else
			return false;
	}
}

template<class T, int size>
int Heap<T, size>::WhichIsPriorChild(int idx)
{
	int left_idx = GetLeftChildIdx(idx);

	if (left_idx > numOfData)
		return -1;
	else if (left_idx == numOfData)
		return left_idx;

	T left_value = dynamicArr[GetLeftChildIdx(idx)];
	T right_value = dynamicArr[GetRightChildIdx(idx)];

	switch (min_max)
	{
	case 1://min heap
		if (left_value < right_value)
			return GetLeftChildIdx(idx);
		else
			return GetRightChildIdx(idx);
	case 2://max heap
		if (left_value > right_value)
			return GetLeftChildIdx(idx);
		else
			return GetRightChildIdx(idx);
	}
}

template<typename T, int size>
bool Heap<T, size>::IsGoDown(int idx, T data)
{
	int child_idx = WhichIsPriorChild(idx);

	if (child_idx < 0)
		return false;

	T value = dynamicArr[child_idx];
	switch (min_max)
	{
	case 1://min heap
		if (value < data)
			return true;
		else
			return false;
	case 2://max heap
		if (value > data)
			return true;
		else
			return false;
	}
}
