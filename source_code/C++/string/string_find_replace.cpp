#include <iostream>
#include <string>
using namespace std;

int main(void)
{
	string st("I am your father!");

	int first_a = st.find('a');
	cout <<"the index of first a : "<< first_a << endl;

	//offset  
	int second_a = st.find('a', 10);
	cout << "the index of second a : " << second_a << endl;

	st.replace(st.find('f'), 6, "foe");
	cout << "string replaced : "<<st << endl;

	return 0;
}