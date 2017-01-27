#include <stdio.h>

int main(void)
{
	//16진수로 bit 그대로 나타낸다면??
	//메모리에는 0x43280000으로 기록....
	//리틀엔디언까지 고려하면....
	//0x00002843으로 기록되어 있겠군요.....
	// 이 비밀을 파헤쳐볼까요??
	float num = 168.0f;

	printf("%f \n", num);

	float num2 = 17.25f;
	printf("%f\n", num2);

	float num3 = 0.51171875f;
	printf("%f\n", num3);

	return 0;
}