package ex1;
import java.util.*;

public class ex1_2 
{

	public static void main(String[] args)
	{
		int number;
		Scanner input = new Scanner(System.in);
		System.out.println("Please insert number: ");
		number = input.nextInt();
		
		int sum = 0;
		while(number != 0)
		{
			sum += number % 10;
			number = number / 10;
		}
		System.out.println(sum);
	}

}
