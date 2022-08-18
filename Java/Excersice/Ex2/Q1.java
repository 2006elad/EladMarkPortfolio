package ex2;
import java.util.Scanner;

public class Q1 {

	public static void main(String[] args)
	{
		String str, subString = "";
		int start = -1;
		Scanner input = new Scanner(System.in);
		System.out.println("Please insert String");
		str = input.nextLine();
		boolean isValid = false;
		while(isValid != true)
		{
			System.out.println("Please insert start");
			start = input.nextInt();
			if(start < 0 || start > str.length() -1)
			{
				System.out.println("Input is invalid");
			}
			else
			{
				isValid = true;
			}
		}
		
//		for(int i=start;i<str.length();i++)
//		{
//			subString += str.charAt(i);
//		}
//		System.out.println(subString);
		StringBuffer subText = new StringBuffer();
		for(int i=start;i<str.length();i++)
		{
			subText.append(str.charAt(i));
		}
		System.out.println(subString);
	}

}
