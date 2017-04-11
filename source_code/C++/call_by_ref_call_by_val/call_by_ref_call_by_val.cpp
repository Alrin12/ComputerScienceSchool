#include <iostream>
using namespace std;

//두 수를 함수 내에서 바꿉니다.
void func_by_value(int a, int b)
{
	int temp = a;
	a = b;
	b = temp;
}

//두 수를 함수 내에서 바꿉니다.
void func_by_ref(int & a, int & b)
{
	int temp = a;
	a = b;
	b = temp;
}

int main(void)
{
	int a = 10;
	int b = 20;
	cout << "before function" << endl;
	cout << "a : " << a << endl;
	cout << " b : " << b << endl<<endl<<endl;

#if 0
	func_by_value(a, b);
#else
	func_by_ref(a, b);
#endif
	cout << "after function" << endl;
	cout << "a : " << a << endl;
	cout << " b : " << b << endl << endl << endl;

	return 0;
}