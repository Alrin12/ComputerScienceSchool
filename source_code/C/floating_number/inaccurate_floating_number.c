#include <stdio.h>

int main(void)
{
	float sum = 0.0f;

	for (int i = 0; i < 100; i++)
		sum += 0.01f;

	printf("%f \n", sum);

	return 0;
}