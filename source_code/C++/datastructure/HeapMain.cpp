#include "Heap.h"

int main(void)
{
	
	//min heap
	Heap<int, 50> heap1("min");

	//max heap
	//Heap<int, 50> heap1("max");

	heap1.Insert(3);
	heap1.Insert(5);
	heap1.Insert(1);
	heap1.Insert(10);
	heap1.Insert(8);
	heap1.Insert(7);
	heap1.Insert(4);
	heap1.Insert(5);
	heap1.Insert(2);
	heap1.Insert(6);
	heap1.Insert(9);

	int end_point1 = heap1.GetNumOfData();

	cout << "정수형 데이터 " << endl;
	for (int i = 0; i < end_point1; i++)
		cout << heap1.Delete() << endl;

	cout << endl << endl;

	//min heap
	//Heap<float, 50> heap2("min");

	//max heap
	Heap<float, 50> heap2("max");

	heap2.Insert(3.14);
	heap2.Insert(5.25);
	heap2.Insert(1.12);
	heap2.Insert(10.124);
	heap2.Insert(8.55);
	heap2.Insert(7.63);
	heap2.Insert(4.23);
	heap2.Insert(5.66);
	heap2.Insert(2.23);
	heap2.Insert(6.16);
	heap2.Insert(9.83);
	

	int end_point2 = heap2.GetNumOfData();

	cout << "실수형 데이터" << endl;
	for (int i = 0; i < end_point2; i++)
		cout << heap2.Delete() << endl;

	return 0;
}
