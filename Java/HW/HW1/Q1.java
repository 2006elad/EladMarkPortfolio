import java.util.*;
public class Q1 
{
	/* Program that count how many times sub string is appears in a string
	 *	In the end the function print count.
	 */
	public static void main(String[] args) 
	{
		String str1, str2;
		int count = 0;
		Scanner input = new Scanner(System.in);
		System.out.println("Please insert String 1");
		str1 = input.nextLine();
		System.out.println("Please insert String 2");
		str2 = input.nextLine();
		for(int i=0;i<=(str1.length() - str2.length());i++)
		{
			if(str1.charAt(i) == str2.charAt(0))
			{
				boolean isSub = true;
				for(int j=1; j<str2.length();j++)
				{
					if(str1.charAt(i + j) != str2.charAt(j))
					{
						isSub = false;
					}
				}
				if(isSub == true)
				{
					count ++;
				}
			}
		}
		System.out.println("Str2 is in Str1 " + count + " Times");
		
	}

}
