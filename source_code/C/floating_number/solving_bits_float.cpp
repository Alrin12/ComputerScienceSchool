#include <stdio.h>

int main(void)
{
	//16������ bit �״�� ��Ÿ���ٸ�??
	//�޸𸮿��� 0x43280000���� ���....
	//��Ʋ�������� ����ϸ�....
	//0x00002843���� ��ϵǾ� �ְڱ���.....
	// �� ����� �����ĺ����??
	float num = 168.0f;

	printf("%f \n", num);

	float num2 = 17.25f;
	printf("%f\n", num2);

	float num3 = 0.51171875f;
	printf("%f\n", num3);

	return 0;
}