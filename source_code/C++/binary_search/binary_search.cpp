#include <iostream>
using namespace std;

int binary_search(int target, int * data, int data_length)
{
	int start = 0;
	int end = data_length - 1;

	while (start <= end)
	{
		int mid = (start + end) / 2;

		if (data[mid] == target)
			return mid;
		else if (data[mid] > target)
			end = mid - 1;
		else
			start = mid + 1;
	}

	return -1;
}

int main(void)
{
	int arr[] = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
	
	int target = 4;
	int length = sizeof(arr) / sizeof(int);
	int idx = binary_search(target, arr, length);
	if (idx == -1)
		cout << "찾는 데이터가 존재하지 않습니다." << endl;
	else
	{
		cout << "index : " << idx << endl;
		cout << "data : " << arr[idx] << endl;
	}

	target = 15;
	idx = binary_search(target, arr, length);
	if (idx == -1)
		cout << "찾는 데이터가 존재하지 않습니다." << endl;
	else
	{
		cout << "index : " << idx << endl;
		cout << "data : " << arr[idx] << endl;
	}


	return 0;
}