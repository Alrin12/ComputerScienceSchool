#pragma once
#include "Stack.h"

class Calculator
{
private:
	char origExp[256];
	char postFixExp[256];
	Stack<char> stackOfOperator;
	Stack<int> stackOfOperand;
	int lenOfOrigExp;
	int lenOfPostFixExp;
private:
	int GetWeight(char ch);
	int CalcTwoOp(int a, int b, char op);
public:
	Calculator();
	~Calculator() {}
	void SetExpression(char * exp);
	const char * GetOrigExp();
	const char * ConvertToPostfix();
	int Calculate();
};
