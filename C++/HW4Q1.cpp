#include <iostream>#include <string.h>using namespace std;void encrypted(char str[]);int main(){	char str[50] = { "3y!!roe$&hT+* -gnaB gi#B eh@T" };	encrypted(str);	return 0;}void encrypted(char str[]){	if (str[0] == '\0')	{		return;	}	else	{		encrypted(str + 1);		if ((str[0] >= 'a' && str[0] <= 'z') || (str[0] >= 'A' && str[0] <= 'Z') || (str[0] >= '0' && str[0] <= '9'))		{			cout << str[0];		}		return;	}	}