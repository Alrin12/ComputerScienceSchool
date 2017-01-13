#include "SortingArray.h"

int main(void)
{
	SortingArray<int, 15> arr;

	arr[0] = 2;
	arr[1] = 5;
	arr[2] = 4;
	arr[3] = 1;
	arr[4] = 8;
	arr[5] = 10;
	arr[6] = 5;
	arr[7] = 3;
	arr[8] = 6;
	arr[9] = 6;
	arr[10] = 5;
	arr[11] = 7;
	arr[12] = 9;
	arr[13] = 12;
	arr[14] = 11;

	/*for (int i = 0; i < arr.arrlen(); i++)
		arr[i] = i+1;*/

	for (int i = 0; i < arr.arrlen(); i++)
		cout << arr[i] << "    ";

	
	cout << '\n';
	//arr.BubbleSort();
	//arr.InsertionSort();
	//arr.SelectionSort();


	//arr.QuickSort();
	arr.MergeSort();

	//cout << "Call Of Exchange : " << arr.GetCallOfExchange() << endl;

	for (int i = 0; i < arr.arrlen(); i++)
		cout << arr[i] << "    ";

	cout << endl;

	return 0;
}
