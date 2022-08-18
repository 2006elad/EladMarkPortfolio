package ex1;
import java.util.*;

public class ex1_3 
{
	public static void main(String[] args)
	{
		int number;
		Scanner input = new Scanner(System.in);
		System.out.println("Please insert number: ");
		number = input.nextInt();
		int new_number;
		new_number = (number % 10) * 100;
		number = number / 10;
		new_number = new_number + (number % 10) * 10;
		number = number / 10;
		new_number = new_number + number;
		System.out.println(new_number);
	}
}
