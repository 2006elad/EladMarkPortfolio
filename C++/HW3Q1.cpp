#include <iostream>
#include <string.h>
using namespace std;

int mystr(char s[], char t[]); //Func that return the how many times t string is in s
bool isStringEqual(char s[], char t[], int i); //Extra func that returning true if t is in s from i index 

int main()
{
	char s[30];
	char t[30];
	cout << "Please enter S string" << endl;
	cin >> s;
	cout << "Please enter T string" << endl;
	cin >> t;
	cout << "T is equal " << mystr(s,t) << " Times in S" << endl;
	return 0;
}

int mystr(char s[], char t[])
{
	int i = 0; // index for s string
	int count = 0;
	while (s[i] != '\0') // While loop until the end of s string
	{
		if (isStringEqual(s, t, i) == true) // check if from s[i] address is equal to t string 
		{
			count++;
		}
		i++;
	}
	return count;
}

bool isStringEqual(char s[], char t[], int i)
{
	if (s[i] == '/0')// make sure that s[i] isn't the end of the string
	{
		return false;
	}

	int j = 0;
	while (t[j] != '\0') // looping till the end of t string
	{
		if (s[i] != t[j]) // if s[i] is equal to t[i] - if not return false
		{
			return false;
		}
		j++;
		i++;
	}
	return true; // because we checked all of t string we know that they are equal
}