#include <iostream>
#include <string>
using namespace std;

int main(void)
{
	char * str = "hello";
	
	string st1(str);
	string st2("world");
	string st3 = st1 + " " + st2;//���ڿ� + ������ ����
	string st4("hello", 4);//���ڿ� �� 4�� ���ڷ� ����
	string st5(st1.begin(), st1.end());

	cout << st3 << endl;
	cout << st4 << endl;
	cout << st5 << endl;

	char * ptr1 = str;
	char * ptr2 = ptr1 + 4;

	string st6(ptr1, ptr2);
	cout << "go to " << st6 << endl;

	return 0;
}