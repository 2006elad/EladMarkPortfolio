#include <iostream>
#include <string.h>

#define MAXLENGTH 100

using namespace std;

//Main Functions
void Plang(char str[]); //Func Pig latin decleration
void Blang(char str[]); //Func B language decleartion

//Extra Functions
void tempStrCreate(char str[], int i, char tempStr[]); // Saving in tempStr the rest string to add it after we doing the changeing
bool isVowel(char oneLetter); // checking if the letter is vowel or not
void CombineTempToStr(char str[], int i ,char tempStr[]); //copy the tempStr to the main string in i place
int endOfTheWord(char str[], int i); // find ' ' or '.' - that are meant to show us in which i we have the end of the word, the func send back the i place
char backspaceOrDot(char str[], int i); // func that send back if we have backspace or dot after the word - than we can add it the the main string after changes

//Extra Functions for Plang func
void strTillVowel(char str[], int i, char tempStr[]); // fill temp str with the letters before the vowel
void fromVowelToTheEndOfTheWord(char str[], int i, char tempStr[]); // fill temp str with the letters before the vowel




int main()
{
	char str[MAXLENGTH];
	int choice;
	cout << "Please choose:" << endl << "1: Pig-Latin \n2: B-Language \n0: Finish \n"; // main menu that takes user choice
	cin >> choice;
	while (choice != 0) // loop until the user insert 0 to exit
	{
		if (choice == 1) // if he choose p latin
		{
			cout << "Please Insert the String: " << endl; // getting from user the string he want to translate
			cin.ignore();
			cin.getline(str, MAXLENGTH);
			Plang(str);
			cout << "\n" << "The sentence in Pig latin is: " << str << "\n" << endl;
		}
		else
		{
			if (choice == 2) // if he choose b language
			{
				cin.ignore();
				cout << "Please Insert the String" << endl; // getting from user the string he want to translate
				cin.getline(str, MAXLENGTH);
				Blang(str);
				cout << "\n" << "The sentence in B language is: " << str << "\n" << endl;
			}
			else // if he put other letter that isn't between 0-2
			{
				cout << "Invalid Choice Please Try Again\n" << endl;
			}
		}
		cout << "Please choose:" << endl << "1: Pig-Latin \n2: B-Language \n0: Finish" << endl; //replay the menu for another choice
		cin >> choice;
	}
	cout <<"\n" << "Good Bye !" << endl;
	return 0;
}
void Blang(char str[])
{
	int i = 0;
	char tempStr[MAXLENGTH];
	while (str[i] != '\0') //loop until we end the sentence
	{
		if (isVowel(str[i]) == true) // check if we have a vowel and then we will change the string with b lang settings
		{
			tempStrCreate(str, i+1 ,tempStr); // we creating  the temp string that after the letter were at
			str[i + 1] = 'b'; // adds b after the letter
			str[i + 2] = str[i]; // adds the vowel itself to the main string
			i = i + 3; // change the i location to the exact place after the changeing
			CombineTempToStr(str, i, tempStr);//combine the main string from i place to paste back the rest of the string
		}
		else
		{
			i++; // if it isn't vowel we are continue
		}
	}
}

void Plang(char str[])
{
	int i = 0, j;
	while (str[i] != '\0') // loop until we are finish the sentence
	{
		if (isVowel(str[i]) == true) // check if the first letter of the word is a vowel if yes we add 'way' to the end of the word, if it isn't we doing isn't vowel settings
		{																		
			char tempStr[MAXLENGTH]; // tempStr for the rest of the string
			j = endOfTheWord(str, i); // j place to found until when the word is finish before we ending (we doing it to find where we saving the tempStr from)
			tempStrCreate(str, j+1, tempStr); // we creating the temp str
			char bOd = backspaceOrDot(str, i); // we saving the ' ' or '.' to add them later after changeing
			str[j] = 'w'; //putting in the main string the p latin for vowel settings
			str[j + 1] = 'a';
			str[j + 2] = 'y';
			str[j + 3] = bOd;
			i = j + 4;
			CombineTempToStr(str, i, tempStr); // combine the rest of the sentence to the main string after changing
		}
		else // if it isn't vowel we are doing p latin setting for non vowel words
		{
			char tempStr[MAXLENGTH]; // tempStr for the rest of the string
			j = endOfTheWord(str, i); //j place to found until when the word is finish before we ending (we doing it to find where we saving the tempStr from)
			tempStrCreate(str, j + 1, tempStr); // we creating the temp str
			char bOd = backspaceOrDot(str, i);// we saving the ' ' or '.' to add them later after changeing
			char tempTillVowel[MAXLENGTH]; // string that save the words until the vowel
			char tempAfterVowel[MAXLENGTH];// string that save the word after the vowel
			strTillVowel(str, i, tempTillVowel);
			fromVowelToTheEndOfTheWord(str, i + strlen(tempTillVowel), tempAfterVowel);
			CombineTempToStr(str, i, tempAfterVowel); //we are putting the aftervowel at the start of the word
			CombineTempToStr(str, i + strlen(tempAfterVowel), tempTillVowel); // now we are putting the till vowel string after till vowel string has pasted (we putting i (start of the word) + the lenth of the after vowel lenth) - to make sure we are pasting in after afterVowel String
			i = i + (strlen(tempTillVowel) + strlen(tempAfterVowel)); // we are change the i to the end of the word
			str[i] = 'a'; // another non vowel word settings
			str[i + 1] = 'y';
			str[i + 2] = bOd; // add backspace or dot
			i = i + 3; //we change the i after we change the word
			CombineTempToStr(str, i, tempStr); // we are pasting the tempStr to the main string after change
		}
	}
}

void tempStrCreate(char str[], int i, char tempStr[])
{
	int j = 0;
	while (str[i] != '\0')
	{
		tempStr[j] = str[i];
		i++;
		j++;
	}
	tempStr[j] = '\0';
}

// Extra Functions
bool isVowel(char oneLetter)
{
	if (oneLetter == 'a' || oneLetter == 'e' || oneLetter == 'i' || oneLetter == 'o' || oneLetter == 'u')
	{
		return true;
	}
	else
	{
		return false;
	}
}

void CombineTempToStr(char str[], int i, char tempStr[])
{
	int j = 0;
	while (tempStr[j] != '\0')
	{
		str[i] = tempStr[j];
		i++;
		j++;
	}
	str[i] = '\0';
}

int endOfTheWord(char str[], int i)
{
	while (str[i] != ' ' && str[i] != '.' )
	{
		i++;
	}
	return i;
}

char backspaceOrDot(char str[], int i)
{
	while (str[i] != ' ' && str[i] != '.')
	{
		i++;
	}
	return str[i];
}

//Extra func for Pig latin
void strTillVowel(char str[], int i, char tempStr[])
{
	int j = 0;
	while (isVowel(str[i]) != true)
	{
		tempStr[j] = str[i];
		i++;
		j++;
	}
	tempStr[j] = '\0';
}

void fromVowelToTheEndOfTheWord(char str[], int i, char tempStr[])
{
	int j = 0;
	while (i < endOfTheWord(str, i))
	{
		tempStr[j] = str[i];
		i++;
		j++;
	}
	tempStr[j] = '\0';
}