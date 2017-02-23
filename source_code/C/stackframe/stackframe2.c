#include <stdio.h>

int add_plus_one_nums(int a, int b)
{
	int c;
	int d;

	__asm
	{
		mov eax, dword ptr[ebp + 8]
		add eax, 1
		mov dword ptr[ebp - 8], eax
		mov ecx, dword ptr[ebp + 12]
		add ecx, 1
		mov dword ptr[ebp - 8 - 12], ecx
	}

	return c + d;
}

int main(int argc, char * argv[])
{
	int a;
	int b;

	__asm
	{
		mov dword ptr[ebp - 8], 5
		mov dword ptr[ebp - 8 - 12], 7
	}

	int result = add_plus_one_nums(a, b);
	printf("(%d+1) + (%d+1) = %d \n", a, b, result);

	return 0;
}


