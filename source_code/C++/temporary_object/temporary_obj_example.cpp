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
	//임시객체도 스택에 할당된다.
	Point(3, 4);

	int num = 10;

	//리턴 시 임시 객체도 스택에
	//eax에는 임시 객체의 address가 저장됨.
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
