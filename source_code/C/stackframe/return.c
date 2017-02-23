#include <stdio.h>

void add_plus_one_nums(int a, int b)
{
	int c = a + 1;
	int d = b + 1;
	__asm
	{
		mov eax, dword ptr[ebp - 8]
		add eax, dword ptr[ebp - 8 - 12]
	}
}

int main(int argc, char * argv[])
{
	int a = 5;
	int b = 7;
	int result;

	add_plus_one_nums(a, b);
	__asm
	{
		mov dword ptr[ebp - 8 - 12 - 12], eax
	}
	printf("(%d+1) + (%d+1) = %d \n", a, b, result);
	return 0;
}




