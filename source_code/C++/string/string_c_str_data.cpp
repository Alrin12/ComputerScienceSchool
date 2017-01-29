#include <iostream>
#include <string>
using namespace std;

int main(void)
{
	string st("abcde");
	cout << "st : " << st << endl;

	const char * str1 = st.c_str();
	const char * str2 = st.data();
	printf("%s \n", str1);
	printf("%s \n", str2);

	cout << '\n' << '\n';

	char * str3 = const_cast<char*>(st.c_str());
	str3[2] = 'b';
	printf("%s \n", str3);
	cout << st << endl;

	return 0;
}