#include "LinkedList.h"
#include <iostream>
using namespace std;

int main(void)
{
	LinkedList<int> list;
	list.Add(2);
	list.Add(3);
	list.Add(1);
	list.Add(5);
	list.Add(10);
	list.Add(7);
	list.Add(2);

	cout <<"데이터의 개수 : "<< list.length() << endl;

	int n;

	if (list.First(&n))
	{
		cout << n<<"    ";
		
		while (list.Next(&n))
		{
			cout << n << "    ";
		}
	}
	cout << endl;

	if (list.First(&n))
	{
		if (n == 2)
			list.Delete();

		while (list.Next(&n))
		{
			if (n == 2)
				list.Delete();
		}
	}
	cout << endl;

	cout << "데이터의 개수 : " << list.length() << endl;

	if (list.First(&n))
	{
		cout << n << "    ";

		while (list.Next(&n))
		{
			cout << n << "    ";
		}
	}
	cout << endl;
	
	return 0;
}
