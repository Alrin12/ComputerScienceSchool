#include <iostream>
#include <string>
using namespace std;

int main(void)
{
	string st1, st2, st3, st4;
	st1 = "abcdefghij";
	cout << "st1 : " << st1 << endl;
	
	//0���� ������
	st2 = st1.substr(0);
	cout << "st2 : " << st2 << endl;

	//5���� ������
	st3 = st1.substr(5, string::npos);
	cout << "st3 : " << st3 << endl;


	//3���� 5��
	st4 = st1.substr(3, 5);
	cout << "st4 : " << st4 << endl;

	return 0;
}