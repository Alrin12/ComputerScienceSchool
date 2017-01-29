#include <iostream>
#include <string>
using namespace std;

int main(void)
{
	string st1("hello");
	st1.insert(1, "abc");
	cout << "st1 : " << st1 << endl;
	
	string st2;
	cin >> st2;
	cout << "st2 : " <<st2<<endl;
	cin.clear();
	cin.ignore(1000, '\n');
	
	string st3;
	getline(cin, st3);
	cout << "st3 : " << st3 << endl;

	return 0;
}
