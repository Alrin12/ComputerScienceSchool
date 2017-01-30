#include <iostream>
#include <string>
using namespace std;

int main(void)
{
	string st = "abcde";
	for (int i = 0; i < st.size(); i++)
		st[i] = 'b';

	cout << "st : " << st << endl;

	return 0;
}