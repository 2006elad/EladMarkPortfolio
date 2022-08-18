import java.util.*;

public class Main 
{
	public static int getChoice(Scanner input)
	{
		boolean isValid = false;
		int choice = -1;
		while(!isValid)
		{
			System.out.println("Please Insert 1 - to create new CardBox\nInsert 2 - to create Plastic Box\nPress 0 - to Exit");
			choice = input.nextInt();
			if(!(0 <= choice && choice <= 2))
			{
				System.out.println("You can only enter choice between 0-2\nPlease Insert Again!");
			}
			else
			{
				isValid = true;
			}
		}
		return choice;
	}

	public static void main(String[] args) 
	{
		Scanner input = new Scanner(System.in);
		ArrayList<Box> boxArray = new ArrayList<Box>();
		Double volume;
		boolean liquidProof;
		boolean isFinish = false;
		
		//Input boxes system
		while(!isFinish)
		{
			int choice = getChoice(input);
			if(choice == 1) // CardBox
			{
				System.out.println("Please insert box volume: ");
				volume = input.nextDouble();
				System.out.println("Is the box liquid Proof? true/false");
				liquidProof = input.nextBoolean();
				CardBox newCardBox = new CardBox(volume, liquidProof);
				boxArray.add(newCardBox);
			}
			else if(choice == 2) // PlasticBox
			{
				System.out.println("Please insert box volume: ");
				volume = input.nextDouble();
				System.out.println("Is the box liquid Proof? true/false");
				liquidProof = input.nextBoolean();
				PlasticBox newPlasticBox = new PlasticBox(volume, liquidProof);
				boxArray.add(newPlasticBox);
			}
			else
			{
				isFinish = true;
			}
		}
		
		System.out.println("The factory produced " + Box.getNumOfProducedProduct() + "Boxes ");
		for(Box oneBox : boxArray)
		{
			System.out.println(oneBox);
		}
		input.close();
	}
}
