#include "Calculator.h"
#include <iostream>
#include <cstring>

Calculator::Calculator()
	: lenOfOrigExp(0), lenOfPostFixExp(0)
{
	memset(origExp, 0, sizeof(origExp));
	memset(postFixExp, 0, sizeof(postFixExp));
}

void Calculator::SetExpression(char * exp)
{
	char expression[256];
	int cnt = 0;
	int len = strlen(exp)+1;
	char filter = ' ';
	for (int i = 0; i < len; i++)
	{
		if (exp[i] == filter)
			continue;

		expression[cnt++] = exp[i];
	}

	strcpy(origExp, expression);
	lenOfOrigExp = strlen(origExp);
}

const char * Calculator::GetOrigExp()
{
	return origExp;
}

int Calculator::GetWeight(char ch)
{
	switch (ch)
	{
	case '*': case '/':
		return 9;
	case '+': case '-':
		return 7;
	case '(':
		return 5;
	}
}

const char * Calculator::ConvertToPostfix()
{
	int cnt = 0;
	for (int i = 0; i < lenOfOrigExp; i++)
	{
		if (isdigit(origExp[i]))
		{
			postFixExp[cnt++] = origExp[i];
			continue;
		}
		
		if (stackOfOperator.IsEmpty() || origExp[i] == '(')
			stackOfOperator.Push(origExp[i]);
		else
		{
			char ch;
			if (origExp[i] == ')')
			{
				while ((ch = stackOfOperator.Pop()) != '(')
					postFixExp[cnt++] = ch;
			}
			else
			{
				if (GetWeight(origExp[i]) > GetWeight(stackOfOperator.Peek()))
					stackOfOperator.Push(origExp[i]);
				else
				{
					while (!stackOfOperator.IsEmpty() && GetWeight(stackOfOperator.Peek()) >= GetWeight(origExp[i]))
					{
						postFixExp[cnt++] = stackOfOperator.Pop();
					}
					stackOfOperator.Push(origExp[i]);
				}
			}

		}
	}
	while (!stackOfOperator.IsEmpty())
	{
		postFixExp[cnt++] = stackOfOperator.Pop();
	}
	lenOfPostFixExp = strlen(postFixExp);
	return postFixExp;
}

int Calculator::CalcTwoOp(int a, int b, char op)
{
	int result = 0;
	switch (op)
	{
	case '+':
		result = a + b;
		break;
	case '-':
		result = a - b;
		break;
	case '*':
		result = a * b;
		break;
	case '/':
		result = a / b;
		break;
	}

	return result;
}

int Calculator::Calculate()
{
	int result = 0;
	int a, b;
	for (int i = 0; i < lenOfPostFixExp; i++)
	{
		if (isdigit(postFixExp[i]))
			stackOfOperand.Push(int(postFixExp[i]-'0'));
		else
		{
			b = stackOfOperand.Pop();
			a = stackOfOperand.Pop();
			result = CalcTwoOp(a, b, postFixExp[i]);
			stackOfOperand.Push(result);
		}
	}

	result = stackOfOperand.Pop();
	return result;
}
