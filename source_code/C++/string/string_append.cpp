#include <iostream>
#include <string>
using namespace std;

int main(void)
{
	string st1("hel");
	st1.append("lo");
	cout << "st1 first : "<< st1 << endl;

	const char * str = "world! adasdasdf";
	st1 += " ";
	st1.append(str, 0, 6);
	cout <<"st1 : " << st1 << endl;

	cout << "\n\n";

	string st2("h");
	string st3;
	st3 = "ello world!";

	for (string::iterator iter = st3.begin(); iter != st3.end(); iter++)
		st2.push_back(*iter);
	cout <<"st2 : "<< st2 << endl;

	return 0;
}
