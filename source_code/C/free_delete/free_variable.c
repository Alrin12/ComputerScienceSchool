#include <stdio.h>

int main(void)
{
	int num = 15;
	int * ptr = &num;
	printf("%d \n", num);

	//��ü�� �����
	free(ptr);

	//printf("%d\n", num);

	return 0;
}