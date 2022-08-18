#include <iostream>
using namespace std;

int sum(int arr[], int n); // main sum function
int countZugi(int num); // count the number of digits that even
int countEiZugi(int num); // count the number of digits that odd

int main()
{
	int arr[8] = { 5532, 3, 849, 5432, 456, 111, 256, 434 };
	int totalSum = sum(arr, 8);
	cout << totalSum;
	return 0;
}

int sum(int arr[], int n)
{
	int totalSum = 0; // sum all of the right indexes values
	if (n == 0) // the recursion stop when the size of the array is zero
	{
		return 0;
	}
	else
	{
		totalSum = sum(arr, n - 1);
		if (countZugi(arr[n - 1]) > countEiZugi(arr[n - 1])) // checks we have more even digits than odd digits
		{
			totalSum = totalSum + arr[n - 1]; // add it to the main sum
		}
		return totalSum; //return the total sum
	}
}

int countZugi(int num)
{
	int count = 0;
	if (num == 0) // if the we finish to check every digits
	{
		return 0;
	}
	else
	{
		count = countZugi(num / 10); //we send each number but without the first digit
		if ((num % 10 ) % 2 == 0) // we check if it even
		{
			count++; // we found an even digit so we add it to the count
		}
		return count; return //the final result
	}
}
int countEiZugi(int num)
{
	int count = 0;
	if (num == 0)
	{
		return 0;
	}
	else
	{
		count = countEiZugi(num / 10); //we send each number but without the first digit
		if ((num % 10) % 2 == 1) // we check if it odd
		{
			count++; // we found an even digit so we add it to the count
		}
		return count; //the final result
	}
}