#include <stdio.h>

int main(void)
{
	int * pnum = (int*)malloc(4);
	*pnum = 15;

	int * ptr = pnum;

	printf("%d \n", *pnum);

	free(ptr);
	/*
	int num = 15;
	int * ptr = &num;
	printf("%d \n", num);

	//��ü�� �����
	free(ptr);
	*/

	//printf("%d\n", num);

	return 0;
}