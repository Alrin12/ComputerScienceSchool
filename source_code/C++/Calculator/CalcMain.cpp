#include "Calculator.h"
#include <iostream>
using namespace std;

int main(void)
{
	char exp[256];
	Calculator calc;
	cin.getline(exp, sizeof(exp));

	calc.SetExpression(exp);
	const char * postExp;
	postExp = calc.ConvertToPostfix();
	cout <<"postfix expression : "<< postExp<<endl;

	int result = calc.Calculate();
	cout << calc.GetOrigExp() << " = " << result << endl;

	return 0;
}