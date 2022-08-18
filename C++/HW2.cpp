#include <iostream>
using namespace std;

const int N = 5;
const int sleeve = 10;

// MAIN FUNCTIONS DECLARATION
void printMenu();
float findMostExpensiveCapsule(float prices[], int size);
//int findStrongestCapsuleInStock(int quantities[], int size, int sleeve);
//void showAllCapsulesInStock(int quantities[], float prices[], int size, int sleeve);
float findValueForMoneyPackage(float prices[], int quantities[], int size, float nis, int sleeve);
//void addMoreCapsules(int quantities[], int size);

//EXTRA FUNCTIONS DECLARTAION
bool endProgramFunc();
void bubble_sort(float priceToArrange[]);
float currentMinPriceFunc(float currentMinPrice, float priceToArrange[]);
bool isAnotherSleeveInTheSamePrice(float prices[], int i);


int main()
{
	printMenu();
	return 0;
}

void printMenu()
{
	int i;
	float prices[N];
	int quantities[N];
	cout << "Welcome to Nesspresso Machine" << endl << "Please Vendor follow the rules to insert the Prices and Quantities of the capsules" << endl;
	for (i = 0; i < N; i++)
	{
		cout << "Please insert Capsule " << i + 1 << " Price" << endl;
		cin >> prices[i];
		cout << "Please insert Capsule " << i + 1 << " Quantity" << endl;
		cin >> quantities[i];
	}

	int option;

	bool endProgram = false;
	while (endProgram != true)
	{
		cout << "Welcome to Nespresso Menu" << endl;
		cout << "Welcome to the main menu, please choose using 1-6" << endl;
		cout << "To find the most expensive capsule enter 1" << endl;
		cout << "To find the strongest capsule enter 2" << endl;
		cout << "To show all the capsule in stock enter 3" << endl;
		cout << "To find the best package for your money enter 4" << endl;
		cout << "To add more capsules enter 5" << endl;
		cout << "To end the program enter 6" << endl;
		cin >> option;

		if (option == 1)
		{


			cout << "look at me";
			float theMostExpesiveCapsulePrice = findMostExpensiveCapsule(prices, N);
			cout << "The most expensive Capsule/s is" << endl;
			for (int i = 0; i < N; i++)
			{
				if (theMostExpesiveCapsulePrice == prices[i])
				{
					cout << i << endl;
				}
			}
			if (endProgramFunc() == true)
			{
				endProgram = true;
			}
		}
		else
		{
			/*
			if (option == 2)
			{
				findStrongestCapsuleInStock(quantities, N, int sleeve);
				menuOptions(prices, quantities);
			}
			else
			{
				if (option == 3)
				{
				showAllCapsulesInStock(quantities, prices, N, int sleeve);
				menuOptions(prices, quantities);
				}
				else
				{ */
			if (option == 4)
			{
				float nis;
				cout << "Please enter the money you want to spend: " << endl;
				cin >> nis;
				float finalPrice = findValueForMoneyPackage(prices, quantities, N, nis, sleeve);
				cout << "The final price is " << nis - finalPrice << endl;
				bool acceptOffer = false;
				bool rightInput = false;
				char acceptChoice;
				while (rightInput != true)
				{
					cout << "Do you want to accept offer?" << endl << "Press Y/N" << endl;
					cin >> acceptChoice;
					if (acceptChoice == 'Y' || acceptChoice == 'y')
					{
						acceptOffer = true;
						rightInput = true;
					}
					else
					{
						if (acceptChoice == 'N' || acceptChoice == 'n')
						{
							acceptOffer = false;
							rightInput = true;
						}
						else
						{
							cout << "Invalid Choice - try again !";
						}
					}
					if (acceptOffer == true)
					{
						cout << "Thank you very much for the purchase! " << endl << "You have " << finalPrice << " Change Left" << endl;
					}
					else
					{
						cout << "Maybe next time you will love our offers!" << endl << "Thanks you!";
					}
					cout << "Please visit our shop Soon next time !";
				}
				if (endProgramFunc() == true)
				{
					endProgram = true;
				}

			}
			/* else
			{
				if (option == 5)
				{
					addMoreCapsules(quantities, N);
					menuOptions(prices, quantities);
				}
				else
				{
					if (option == 6)
					{
						cout << "Thank you for using Nespresso Software - GOODBYE";
						return;
					}
					else
					{
						cout << "Invalid Choice! Try Again..." << endl;
					}
				}
			}*/
		}
	}
}

//MAIN FUNCTIONS

float findMostExpensiveCapsule(float prices[], int size)
{
	int i;
	float theMostExpesiveCapsulePrice = 0.0;
	for (i = 0; i < size; i++)
	{
		if (prices[i] > theMostExpesiveCapsulePrice)
		{
			theMostExpesiveCapsulePrice = prices[i];
		}
	}
	return theMostExpesiveCapsulePrice;

}
/*
int findStrongestCapsuleInStock(int quantities[], int size, int sleeve)
{
	return 0;

}
void showAllCapsulesInStock(int quantities[], float prices[], int size, int sleeve)
{

}
*/
float findValueForMoneyPackage(float prices[], int quantities[], int size, float nis, int sleeve)
{
	int i;
	int sleeveQuantitiesArr[N]; // Arr of num of sleeves in every type of coffe
	float oneSleevePriceArr[N]; // Arr of prices of total one type of sleeves prices
	for (i = 0; i < N; i++)
	{
		sleeveQuantitiesArr[i] = quantities[i] / sleeve;
		oneSleevePriceArr[i] = prices[i] * sleeve;
	}
	float leftChange = nis;
	int sumOfSleeves = 0;
	float cheapestSleeve = 0;
	float priceToArrangeArr[N];
	for (i = 0; i < N; i++)// sort the prices
	{
		priceToArrangeArr[i] = oneSleevePriceArr[i];
	}
	bubble_sort(priceToArrangeArr); //Sort the arr
	cheapestSleeve = currentMinPriceFunc(cheapestSleeve, priceToArrangeArr); //insert the first min price to compare
	int counter = N;
	bool thereIsEnoughMoney = true;
	int sleeveCounter;
	bool sleeveQuantitiesCheck[N] = { true, true, true, true, true };
	cout << "The best offer to gain the highest sleeves is:" << endl;
	while (counter > 0 && thereIsEnoughMoney == true) //counter till we end our types of coffee, it can go few times on the arr
	{
		i = 0;
		sleeveCounter = 0;
		while (i < N && thereIsEnoughMoney == true) // go everytime from the start of the arr to check everything we can gain in the arr
		{
			if (cheapestSleeve == oneSleevePriceArr[i]) // check if the current min price is equal to price arr, it tries to make sure there isn't any coffee types in the same price
			{
				if (sleeveQuantitiesCheck[i] == true) // if there is sleeve left
				{
					if (leftChange - oneSleevePriceArr[i] > 0) // make sure the is enough change
					{
						leftChange = leftChange - oneSleevePriceArr[i]; //reduce one sleeve from left money
						sleeveCounter++; // count the num of sleeve were bought
						sleeveQuantitiesArr[i] --; // reduce the quantity of sleeves
						if (sleeveQuantitiesArr[i] == 0)
						{
							sleeveQuantitiesCheck[i] = false;
							cout << "From Coffee type number " << i + 1 << " you can buy " << sleeveCounter << " sleeves" << endl;
							if (isAnotherSleeveInTheSamePrice(oneSleevePriceArr, i) == true)
							{
								sumOfSleeves = sumOfSleeves + sleeveCounter; //Sum of all sleeves that we offering
								sleeveCounter = 0;
							}
						}
					}
					else
					{
						thereIsEnoughMoney = false; //stop the first while
						sumOfSleeves = sumOfSleeves + sleeveCounter;
						cout << "From Coffee type number " << i + 1 << " you can buy " << sleeveCounter << " sleeves" << endl;
					}
				}
				else
				{
					i++; // If coffee type empty of sleeves and we still have enough money - because we know that isAnotherSleeve is true - we continue
				}
			}
			else
			{
				i++; // If the coffee isn't the right one we still have enough money  we going to the next one  - because we know that isAnotherSleeve is true - we continue
			}
		}
		if (counter != 0) // make sure that counter isn't end (to not messed up the min func and make sure that there is another sleeve in the same price
		{
			if (isAnotherSleeveInTheSamePrice(oneSleevePriceArr, i) != true)
			{
				cheapestSleeve = currentMinPriceFunc(cheapestSleeve, priceToArrangeArr);
				counter--;
				sumOfSleeves = sumOfSleeves + sleeveCounter; //Sum of all sleeves that we offering
			}
		}
	}
	cout << "Total Sleeves in the offer " << sumOfSleeves << endl;
	return leftChange;
}
/*
 void addMoreCapsules(int quantities[], int size)
{

}
*/

//EXTRA FUNCTIONS
bool endProgramFunc()
{
	bool rightInput = false;
	bool choice;
	char end;
	while (rightInput != true)
	{
		cout << "Want to end program? Y/N";
		cin >> end;
		if (end == 'Y' || end == 'y')
		{
			choice = true;
			rightInput = true;
		}
		else
		{
			if (end == 'N' || end == 'n')
			{
				choice = true;
				rightInput = true;
			}
			else
			{
				cout << "Invalid Choice - try again !";
			}
		}
	}
	return choice;
}

float currentMinPriceFunc(float currentMinPrice, float ArrangedPricesArr[]) // arrange the sleeve prices and send the min price
{
	for (int i = 0; i < N; i++)
	{
		if (ArrangedPricesArr[i] > currentMinPrice) // Make sure the price is bigger the min price
		{
			return ArrangedPricesArr[i];
		}
	}
}
void bubble_sort(float priceToArrangeArr[])// sort the prices of sleeve arr for min
{
	int i, j;
	float tmp;
	for (i = N - 1; i > 0; i--)
	{
		for (j = 0; j < i; j++)
		{
			if (priceToArrangeArr[j] > priceToArrangeArr[j + 1])
			{
				tmp = priceToArrangeArr[j + 1];
				priceToArrangeArr[j + 1] = priceToArrangeArr[j];
				priceToArrangeArr[j] = tmp;
			}
		}
	}
}
bool isAnotherSleeveInTheSamePrice(float oneSleevePriceArr[], int i) // check if there is another sleeve in the same price
{
	for (int j = i; j < N; j++)
	{
		if (oneSleevePriceArr[j] == oneSleevePriceArr[i])
		{
			return true;
		}
	}
	return false;
}