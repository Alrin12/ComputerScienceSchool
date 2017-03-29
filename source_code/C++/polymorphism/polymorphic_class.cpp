#include <iostream>
using namespace std;

class Animal
{
public:
	virtual void Say()
	{
		cout << "I say ......" << endl;
	}
};

class Dog : public Animal
{
public:
	virtual void Say()
	{
		cout << "I say 港港" << endl;
	}
};

class Cat : public Animal
{
public:
	virtual void Say()
	{
		cout << "I say 具克 具克" << endl;
	}
};

class Duck : public Animal
{
public:
	virtual void Say()
	{
		cout << "I say 残残" << endl;
	}
};

class Lion : public Animal
{

};

int main(int argc, char * argv[])
{
	Animal * ani_arr[4];

	Animal * dog_ptr = new Dog();
	Animal * cat_ptr = new Cat();
	Animal * duck_ptr = new Duck();
	Animal * lion_ptr = new Lion();

	ani_arr[0] = dog_ptr;
	ani_arr[1] = cat_ptr;
	ani_arr[2] = duck_ptr;
	ani_arr[3] = lion_ptr;

	int len_arr = sizeof(ani_arr) / sizeof(Animal);

	for (int i = 0; i < len_arr; i++)
		ani_arr[i]->Say();

	return 0;
}