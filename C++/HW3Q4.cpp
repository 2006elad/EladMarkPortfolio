#include <iostream>

using namespace std;

int sumAllZugi(int arr[], int size);

int main()
{
	int arr[10];
	int size = 10;
	cout << "enter 10 numbers";
	for (int i = 0; i < size - 1; i++)
	{
		cin >> arr[i];
	}
	cout << "sum of all of zugi is: " << sumAllZugi(arr, size -1);
	return 0;
}
int sumAllZugi(int arr[], int size)
{
	int sum = 0;
	if (size -1 == 0)
	{
		if (arr[1] % 2 == 0 && arr[0] % 2 == 0)
		{
			return arr[0] + arr[1];
		}
		else
		{
			if (arr[1] % 2 == 0)
			{
				return arr[1];
			}
			else
			{
				if (arr[0] % 2 == 0)
				{
					return arr[0];
				}
				else
				{
					return 0;
				}
			}
		}
	}
	else
	{
		if (arr[size] % 2 == 0)
		{
			sum = sumAllZugi(arr, size -1) + arr[size];
		}
		else
		{
			sum = sumAllZugi(arr, size -1);
		}
	}
	return sum;
}