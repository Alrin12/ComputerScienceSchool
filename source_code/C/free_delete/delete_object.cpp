#include <iostream>
using namespace std;

class INT
{
public:
	int n;
public:
	INT(int num = 0)
		: n(num)
	{}
	/*
	INT& operator=(int num)
	{
		n = num;
	}
	*/
};

int main(void)
{
	/*
	INT * num = new INT(5);
	INT * ptr = num;
	cout << num->n<<endl;
	*/

	INT num = 15;
	INT * ptr = &num;
	
	cout << num.n<<endl;

	//객체를 지운다
	delete ptr;

	//cout << num.n<<endl;

	return 0;
}