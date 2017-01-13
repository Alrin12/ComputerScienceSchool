#pragma once
#include <iostream>
using namespace std;

template<typename T>
class Queue
{
private:
	class Node
	{
	public:
		T data;
		Node * next;
		Node() : next(0) {}
		Node(T d) : data(d), next(0) {}
	};

public:
	Node * head;
	Node * tail;

	Queue() : head(0), tail(0) { }
	bool IsEmpty();
	void Enqueue(T d);
	T Dequeue();
	T Peek();
};

template<typename T>
bool Queue<T>::IsEmpty()
{
	if (head == 0)
		return true;

	return false;
}

template<typename T>
void Queue<T>::Enqueue(T d)
{
	Node * newNode = new Node(d);

	if (head == 0)
	{
		head = newNode;
		tail = newNode;
		return;
	}

	tail->next = newNode;
	tail = newNode;
}

template<typename T>
T Queue<T>::Dequeue()
{
	if (IsEmpty())
	{
		cout << "Error!" << endl;
		exit(-1);
	}

	Node * delNode = head;
	T retData = delNode->data;

	head = head->next;
	delete delNode;
	return retData;
}

template<class T>
T Queue<T>::Peek()
{
	if (IsEmpty())
	{
		cout << "Error!" << endl;
		exit(-1);
	}

	return head->data;
}
