#include <stdio.h>

typedef int(*funcPtr)(int, int);

int addTwoPtr(int n1, int n2)
{
	return n1 + n2;
}

typedef struct __Pseudo__
{
	int a;
	int b;
	funcPtr objFunc;
}Pseudo;

int main(void)
{
	Pseudo obj = { 5, 2, addTwoPtr };
	int value = obj.objFunc(obj.a, obj.b);
	printf("The value got from object's method :  %d \n", value);
	return 0;
}
