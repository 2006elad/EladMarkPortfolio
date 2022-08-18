package ex1;
import java.util.*;

public class ex1_1 
{

	public static void main(String[] args) 
	{
		String name;
		double dollarRate, euroRate;
		int nis;
		boolean isDollar;
		Scanner input = new Scanner(System.in);
		System.out.println("Please insert your Name: ");
		name = input.nextLine();
		
		System.out.println("Please insert dollar Rate: ");
		dollarRate = input.nextDouble();
		
		System.out.println("Please insert euro Rate: ");
		euroRate = input.nextDouble();
				
		System.out.println("Please insert nis you have: ");
		nis = input.nextInt();
				
		System.out.println("Do you want to show in dollar Rate?: ");
		isDollar = input.nextBoolean();
		
		if(isDollar == true)
		{
			System.out.print(name + " " + nis / dollarRate);
		}
		else
		{
			System.out.print(name + " " + nis / euroRate);
		}		
	}

}
