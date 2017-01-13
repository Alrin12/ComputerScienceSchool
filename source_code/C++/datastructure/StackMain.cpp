#include "Stack.h"
#include <iostream>
using namespace std;

int main(void)
{
	Stack<int> stack;

	stack.Push(1);
	stack.Push(2);
	stack.Push(3);
	stack.Push(4);
	stack.Push(5);

	while (!stack.IsEmpty())
	{
		cout << stack.Pop()<<endl;
	}

	return 0;
}
