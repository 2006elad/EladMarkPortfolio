#include <iostream>
#include <string.h>

using namespace std;

#define ROW 4
#define COLUMN 3
#define SIZE 10

int isParmotazia(int arr1[][COLUMN], int arr2[][COLUMN], int row, int column);
void arrSfarotTimes(int arrSfarot[], int arr[][COLUMN]);
int main()
{
	int arr1[ROW][COLUMN] = { {1, 1, 4} , {2, 2, 3}, {3, 3, 2} , {4, 4, 1} };
	int arr2[ROW][COLUMN] = { {4,1,2}, {2,4,3} , {3,2,4} , {1,1,3} };
	if (isParmotazia(arr1, arr2, ROW, COLUMN) == 0)
	{
		cout << "No Parmotazia" << endl;
	}
	else
	{
		cout << "It is Parmotazia" << endl;
	}
	return 0;
}

int isParmotazia(int arr1[][COLUMN], int arr2[][COLUMN], int row, int column)
{
	int i, j;
	bool isEqual = true;
	for (i = 0; i < ROW; i++)
	{
		for (j = 0; i < COLUMN; i++)
		{
			if (arr1[i][j] != arr2[i][j])
			{
				isEqual = false;
			}
		}
	}
	if (isEqual == true)
	{
		return 0;
	}

	int arrSfarotNum1[SIZE];
	int arrSfarotNum2[SIZE];
	arrSfarotTimes(arrSfarotNum1, arr1);
	arrSfarotTimes(arrSfarotNum2, arr2);
	for (i = 0; i < SIZE; i++)
	{
		if (arrSfarotNum1[i] != arrSfarotNum2[i])
		{
			return 0;
		}
	}
	return 1;
}
void arrSfarotTimes(int arrSfarot[], int arr[][COLUMN])
{
	int i, j, index;
	for (i = 0; i < ROW; i++)
	{
		for (j = 0; j < COLUMN; i++)
		{
			arrSfarot[arr[i][j]]++;
		}
	}
}
