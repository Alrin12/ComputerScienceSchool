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
		cout << "1 ��° ����� " << from << "���� " << to <<
			"�� �̵�" << endl;
		return;
	}

	HanoiTower(from, to, by, num - 1);
	cout << num << " ��° ����� " << from << "���� " << to <<
		"�� �̵�" << endl;
	HanoiTower(by, from, to, num - 1);
}