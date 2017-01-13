#include <iostream>
using namespace std;

void HanoiTower(char from, char by, char to, int num);

int main(void)
{
	int n;
	while (1)
	{
		cin >> n;

		if (n == 0)
			break;

		HanoiTower('A', 'B', 'C', n);
	}
	return 0;
}

void HanoiTower(char from, char by, char to, int num)
{
	if (num == 1)
	{
		cout << "1 번째 쟁반이 " << from << "에서 " << to <<
			"로 이동" << endl;
		return;
	}

	HanoiTower(from, to, by, num - 1);
	cout << num << " 번째 쟁반이 " << from << "에서 " << to <<
		"로 이동" << endl;
	HanoiTower(by, from, to, num - 1);
}