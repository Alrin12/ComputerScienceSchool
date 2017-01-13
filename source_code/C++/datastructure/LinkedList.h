#pragma once

template<typename T>
class LinkedList
{
	class Node
	{
	public:
		T data;
		Node * next;

		Node() { next = 0; }
		Node(T d) : data(d) { next = 0; }
	};
private:
	Node * head;
	Node * tail;
	Node * current;
	Node * before;
	int numOfData;

public:
	LinkedList()
		: current(0), before(0), numOfData(0)
	{
		Node * dummy = new Node();
		head = dummy;
		tail = dummy;
	}
	void Add(T d);
	bool First(T * d);
	bool Next(T * d);
	T Delete();
	int length()
	{
		return numOfData;
	}
};

template<typename T>
void LinkedList<T>::Add(T d)
{
	Node * newNode = new Node(d);

	tail->next = newNode;
	tail = newNode;
	numOfData++;
}

template<typename T>
bool LinkedList<T>::First(T * d)
{
	before = head;
	current = head->next;

	if (current != 0)
	{
		*d = current->data;
		return true;
	}

	return false;
}

template<typename T>
bool LinkedList<T>::Next(T * d)
{
	if (current->next == 0)
		return false;

	before = current;
	current = current->next;
	*d = current->data;
	return true;
}

template<typename T>
T LinkedList<T>::Delete()
{
	Node * delNode = current;
	T retData = delNode->data;

	before->next = current->next;
	current = before;
	numOfData--;
	delete delNode;
	return retData;
}
