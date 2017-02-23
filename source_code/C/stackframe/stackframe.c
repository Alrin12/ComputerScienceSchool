#include <stdio.h>

int add_plus_one_nums(int a, int b)
{
	int c = a + 1;
	int d = b + 1;
	return c + d;
}

int main(int argc, char * argv[])
{
	int a = 5;
	int b = 7;

	int result = add_plus_one_nums(a, b);
	printf("(%d+1) + (%d+1) = %d \n",a, b, result);
	return 0;
}




