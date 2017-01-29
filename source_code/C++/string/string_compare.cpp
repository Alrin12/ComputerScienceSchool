#include <iostream>
#include <string>
using namespace std;

int main(void)
{
	string st1 = "abcde";
	string st2 = st1;
	cout <<"st2 : "<< st2 << endl;
	cout << st2.size()  << endl;
	cout << st2.capacity() << endl;

	cout << endl;

	string st3("fghij");
	cout << "st3 before : "<<st3 << endl;

	st3 = st2;
	cout << "st3 after : " << st3 << endl;
	cout << endl;

	if (!st2.compare(st3))
		cout << "두 문자열은 같습니다" << endl;
	else if (st2.compare(st3) == -1)
		cout << "st2 < st3" << endl;
	else
		cout << "st2 > st3" << endl;

	cout << endl;

	char strArr[10];
	st2.copy(strArr, st2.size());

	for (int i = 0; i < st2.size(); i++)
		cout << strArr[i];

	return 0;
}
