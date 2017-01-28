#include "PriorityQueue.h"

int main(void)
{
	//min heap 이용
	PriorityQueue<int, 20> pq1("min");

	//max heap 이용
	//PriorityQueue<int, 20> pq1("max");

	pq1.Enqueue(3);
	pq1.Enqueue(7);
	pq1.Enqueue(2);
	pq1.Enqueue(1);
	pq1.Enqueue(9);
	pq1.Enqueue(5);
	pq1.Enqueue(8);
	pq1.Enqueue(10);
	pq1.Enqueue(5);
	pq1.Enqueue(6);
	pq1.Enqueue(4);

	int end_point1 = pq1.GetNumOfData();

	cout << "정수형 데이터" << endl;
	for (int i = 0; i < end_point1; i++)
	{
		cout << pq1.Dequeue() << endl;
	}

	cout << endl << endl;

	//min heap 이용
	PriorityQueue<double, 20> pq2("min");

	//max heap 이용
	//PriorityQueue<double, 20> pq2("max");

	pq2.Enqueue(3.125235);
	pq2.Enqueue(7.252355);
	pq2.Enqueue(2.6262626);
	pq2.Enqueue(1.6236236);
	pq2.Enqueue(9.724567);
	pq2.Enqueue(5.6443347345);
	pq2.Enqueue(8.73345343);
	pq2.Enqueue(10.72453563343);
	pq2.Enqueue(5.1235152321);
	pq2.Enqueue(6.62346234);
	pq2.Enqueue(4.263442426);

	int end_point2 = pq2.GetNumOfData();

	cout << "실수형 데이터" << endl;
	for (int i = 0; i < end_point2; i++)
	{
		cout << pq2.Dequeue() << endl;
	}

	return 0;
}