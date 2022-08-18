#include <iostream>
using namespace std;

struct Node 
{
	int data;
	bool boom;
	Node* next;
};

int xBoom(Node* head, int x);
bool weHaveOnlyOne(Node* headOfCheck);
Node* add_first(Node* head);
Node* add_last(Node* current);
void freeList(Node* head, Node* last);
void printList(Node* head);

int main()
{
	cout << "Welcome To Xboom !!!" << endl;
	int numToInsert;
	int count = 0;
	Node* cur;
	Node* head = NULL;

	cout << "Please enter How much Nums you want to insert: " << endl;
	cin >> numToInsert;

	if (numToInsert == 0)
	{
		cout << "List Is Empty";
		return 0;
	}
	
	cout << "Please Enter Numbers " << endl;
	head = add_first(head);

	if (numToInsert == 1)
	{
		cout << "The Final Result is " << head->data;
		delete head;
		return 0;
	}

	cur = head;
	count++;

	while (count < numToInsert)
	{
		cur = add_last(cur);
		count++;
	}
	
	Node* last = cur;
	printList(head);

	cur->next = head;

	int x;
	cout << "Please enter jump number" << endl;
	cin >> x;

	cout << "The Final Result is " << xBoom(head, x);
	freeList(head, last);
	return 0;
}

Node* add_first(Node* head)
{
	Node* newNode = new Node;
	if (newNode == NULL)
		return head;
	cin >> newNode->data;
	newNode->boom = false;
	newNode->next = NULL;
	head = newNode;
	return head;
}

Node* add_last(Node* current)
{
	Node* newNode = new Node;
	if (newNode == NULL)
		return NULL;
	cin >> newNode->data;
	newNode->boom = false;
	newNode->next = NULL;
	current->next = newNode;
	current = newNode;
	return current;
}

void printList(Node* head)
{
	Node* currentNode = head;
	if (currentNode == NULL)
	{
		cout << "The list is empty.\n";
		exit(0);
	}
	else
	{
		cout << currentNode->data;
		currentNode = currentNode->next;
		while (currentNode != NULL)
		{
			cout << " -> " << currentNode->data;
			currentNode = currentNode->next;
		}
		cout << endl;
	}
}

int xBoom(Node* head, int x)
{
	Node* cur = head;
	bool isFinish = false;
	while (isFinish != true)
	{
		int count = 0;
		while (count != x)
		{
			if (cur->boom == false)
			{
				cur = cur->next;
				count++;
			}
			else
			{
				cur = cur->next;
			}
		}
		cur->boom = true;
		if (weHaveOnlyOne(cur) == true)
		{
			isFinish = true;
		}
	}
	return head->data;
}
bool weHaveOnlyOne(Node* headOfCheck)
{
	Node* cur = headOfCheck->next;
	while (cur != headOfCheck)
	{
		if (cur->boom == true)
		{
			return false;
		}
		cur = cur->next;
	}
	return true;
}

void freeList(Node* head, Node* last)
{
	Node* tempNode;
	while (head != last)
	{
		tempNode = head->next;
		delete head;
		head = tempNode;
	}
	delete last;
}