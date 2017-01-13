#include "Queue.h"

int main(void)
{
	Queue<int> queue;

	queue.Enqueue(1);
	queue.Enqueue(2);
	queue.Enqueue(3);
	queue.Enqueue(4);
	queue.Enqueue(5);

	while (!queue.IsEmpty())
	{
		cout << queue.Dequeue() << endl;
	}

	return 0;
}