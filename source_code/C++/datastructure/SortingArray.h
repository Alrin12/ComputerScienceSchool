#pragma once
#include <iostream>
using namespace std;

template<class T, int n>
class SortingArray
{
private:
	T arr[n];
	int arrLen;
	SortingArray(const SortingArray& arr) {}
	SortingArray& operator=(const SortingArray& arr) {}
	int callOfExchange;
public:
	SortingArray() : arrLen(n), callOfExchange(0) {}
	T operator[](int idx) const;
	T& operator[](int idx);
	int arrlen() { return arrLen; }
	int GetCallOfExchange() { return callOfExchange; }

	//단순 정렬 알고리즘
	void BubbleSort();
	void InsertionSort();
	void SelectionSort();

	//divide and conquer
	void MergeSort();
	void QuickSort();

private:
	//모든 정렬이 같이 쓰는 함수
	void SwapIdx(int& a, int& b);
	void Swap(T& a, T& b);

	//Quicksort 구현 함수
	void quicksort(int start, int end);
	int QsortExchange(int start, int end);
	int GetPivot(int start, int end);

	//Mergesort 구현 함수
	void mergesort(int start, int end);
	void MergeTwoSection(int start, int mid, int end);
};

template<class T, int n>
T SortingArray<T, n>::operator[](int idx) const
{
	if (idx<0 || idx > arrLen - 1)
	{
		cout << "Stack Memory Error!" << endl;
		exit(-1);
	}

	return arr[idx];
}

template<class T, int n>
T& SortingArray<T, n>::operator[](int idx)
{
	if (idx < 0 || idx > arrLen - 1)
	{
		cout << "Stack Memory Error!" << endl;
		exit(-1);
	}

	return arr[idx];
}

template<class T, int n>
void SortingArray<T, n>::SwapIdx(int& a, int& b)
{
	int temp = a;
	a = b;
	b = temp;
}

template<class T, int n>
void SortingArray<T, n>::Swap(T& a, T& b)
{
	T temp = a;
	a = b;
	b = temp;
}

template<class T, int n>
void SortingArray<T, n>::BubbleSort()
{
	for (int i = 0; i < arrlen() - 1; i++)
	{
		for (int j = 0; j < arrlen() - i - 1; j++)
		{
			if (arr[j] > arr[j + 1])
			{
				T temp = arr[j];
				arr[j] = arr[j + 1];
				arr[j + 1] = temp;
			}
		}
	}
}

template<class T, int n>
void SortingArray<T, n>::InsertionSort()
{
	//정렬되어 있는 배열에 정렬 안 된 부분을 "삽입(insertion)"한다.

	T unsortedData;
	int properIdx = 0;

	for (int i = 1; i < arrLen; i++)
	{
		unsortedData = arr[i];
		properIdx = 0;
		for (int j = i - 1; j >= 0; j--)
		{
			if (arr[j] > unsortedData)
				arr[j + 1] = arr[j];
			else
			{
				properIdx = j+1;
				break;
			}
		}
		arr[properIdx] = unsortedData;
	}
}

template<class T, int n>
void SortingArray<T, n>::SelectionSort()
{
	//맨 왼쪽부터 하나씩 최솟값을 "선택(selection)"해 채운다

	int minIdx = 0;

	for (int i = 0; i < arrLen - 1; i++)
	{
		minIdx = i;
		for (int j = i + 1; j < arrLen; j++)
		{
			if (arr[j] < arr[minIdx])
				minIdx = j;
		}
		Swap(arr[i], arr[minIdx]);
	}
}

template<class T, int n>
void SortingArray<T, n>::MergeTwoSection(int start, int mid, int end)
{
	int lIdx = start;
	int rIdx = mid + 1;
	int allocated = (end - start) + 1;

	T * tempArr = new T[allocated];

	int tempIdx = 0;
	for (int i = 0; i < allocated; i++)
	{
		if (arr[lIdx] < arr[rIdx])
		{
			tempArr[i] = arr[lIdx++];

			if (lIdx > mid)
			{
				tempIdx = i+1;
				break;
			}
		}
		else
		{
			tempArr[i] = arr[rIdx++];

			if (rIdx > end)
			{
				tempIdx = i + 1;
				break;
			}
		}
	}

	if (lIdx > mid)
	{
		for (int i = rIdx; i <= end; i++)
			tempArr[tempIdx++] = arr[i];
	}

	if (rIdx > end)
	{
		for (int i = lIdx; i <= mid; i++)
			tempArr[tempIdx++] = arr[i];
	}

	tempIdx = 0;
	for (int i = start; i <= end; i++)
		arr[i] = tempArr[tempIdx++];

	delete[] tempArr;
}

template<class T, int n>
void SortingArray<T, n>::MergeSort()
{
	mergesort(0, arrLen - 1);
}

template<class T, int n>
void SortingArray<T, n>::mergesort(int start, int end)
{
	if (start >= end)//탈출조건
		return;

	int mid = (start + end) / 2;

	mergesort(start, mid);
	mergesort(mid + 1, end);

	MergeTwoSection(start, mid, end);
}

template<class T, int n>
int SortingArray<T, n>::GetPivot(int start, int end)
{
	int mid = (start + end) / 2;

	int idxArr[3] = { start, mid, end };

	if (arr[idxArr[0]] > arr[idxArr[1]])
		SwapIdx(idxArr[0], idxArr[1]);
	if (arr[idxArr[1]] > arr[idxArr[2]])
		SwapIdx(idxArr[1], idxArr[2]);
	if (arr[idxArr[0]] > arr[idxArr[1]])
		SwapIdx(idxArr[0], idxArr[1]);

	return idxArr[1];
}

template<class T, int n>
void SortingArray<T, n>::QuickSort()
{
	quicksort(0, arrLen-1);
}


template<class T, int n>
void SortingArray<T, n>::quicksort(int start, int end)
{
	if (start >= end)//탈출조건
		return;

	int pivot = QsortExchange(start, end);

	quicksort(start, pivot - 1);
	quicksort(pivot + 1, end);
}

template<class T, int n>
int SortingArray<T, n>::QsortExchange(int start, int end)
{
	callOfExchange++;

	//pivot을 start로 고정하는 것과 세 점 중 하나를 고를 때 함수 호출 횟수를 확인해보자
	int pIdx = GetPivot(start, end);
	Swap(arr[start], arr[pIdx]);

	//pivot은 무조건 start로 고정
	T pivot = arr[start];
	int low = start + 1;
	int high = end;

	while (low <= high)
	{
		while (arr[low] <= pivot && low <= end)
			low++;

		while (arr[high] >= pivot && high >= (start + 1))
			high--;

		if (low <= high)
			Swap(arr[low], arr[high]);
	}

	Swap(arr[start], arr[high]);

	return high;
}
