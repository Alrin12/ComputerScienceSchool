#pragma once
#include <iostream>
using namespace std;

template<typename T>
class Stack
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

private:
	Node * head;

public:
	Stack() : head(0) {}
	bool IsEmpty();
	void Push(T d);
	T Pop();
	T Peek();
};

template<typename T>
bool Stack<T>::IsEmpty()
{
	if (head == 0)
		return true;

	return false;
}

template<typename T>
void Stack<T>::Push(T d)
{
	Node * newNode = new Node(d);

	newNode->next = head;
	head = newNode;
}

template<typename T>
T Stack<T>::Pop()
{
	if (IsEmpty())
	{
		cout << "Pop Error!" << endl;
		exit(-1);
	}

	Node * delNode = head;
	T retData = delNode->data;

	head = head->next;
	delete delNode;
	return retData;
}

template<typename T>
T Stack<T>::Peek()
{
	if (IsEmpty())
	{
		cout << "Peek Error!" << endl;
		exit(-1);
	}

	T retData = head->data;
	return retData;
}

