#include <iostream>
using namespace std;

#define RVO 0
#define RETURN 0

class Point
{
public:
	Point(int x = 0, int y = 0)
	{
		this->x = x;
		this->y = y;
	}
private:
	int x, y;
};

Point func()
{
	Point p1(1, 2);
	//�ӽð�ü�� ���ÿ� �Ҵ�ȴ�.
	Point(3, 4);

	int num = 10;

	//���� �� �ӽ� ��ü�� ���ÿ�
	//eax���� �ӽ� ��ü�� address�� �����.
	return p1;
}

int main(void)
{
#if RVO
	Point p1 = func();
#elif !RVO && RETURN
	Point p1;
	p1 = func();
	int num = 10;
#else
	int num = 10;
	func();
#endif

	return 0;
}
