package ex2;
import java.util.*;

public class Q2 
{
	public static void main(String[] args) 
	{
		Scanner input = new Scanner(System.in);
		String str1, str2;
		System.out.println("Please insert String 1");
		str1 = input.nextLine();
		System.out.println("Please insert String 2");
		str2 = input.nextLine();
		if(str1.length() != str2.length())
		{
			System.out.println("Str2 isn't mirror string");
		}
		else
		{
			boolean isMirror = true;
			int j = str2.length() - 1;
			for(int i = 0; i<str1.length();i++)
			{	
				if(str1.charAt(i) != str2.charAt(j))
				{
						isMirror = false;
				}
				j--;
			}
			if(isMirror == true)
			{
				System.out.println("Str2 is mirror string");
			}
			else
			{
				System.out.println("Str2 isn't mirror string");
			}
		}
		input.close();
	}

}
