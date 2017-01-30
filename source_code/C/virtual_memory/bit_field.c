#include <stdio.h>

#define TRUE     1
#define FALSE    0

//bitfield : �ڷ����� bit ������ �ɰ� ����!!!
struct __str_data__
{
	// : num --> bits ���� �ǹ��Ѵ�.
	unsigned char capacity : 5;
	unsigned char b_small : 3;
};

typedef struct __str_data__ str_data;

int main(int argc, char ** argv)
{
	str_data st_d = { 12, TRUE };
	
	printf("capacity(how many bytes left) : %d bytes \n", st_d.capacity);
	
	switch (st_d.b_small)
	{
	case TRUE:
		printf("The string is a small string! \n");
		break;
	case FALSE:
		printf("The string is a normal string! \n");
		break;
	}

	return 0;
}