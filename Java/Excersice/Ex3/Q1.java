package ex3;

public class Q1 
{
	/**
	 * 
	 * @param times - how much times print char
	 * @param ch - char we want to print
	 * @return The function will print the char in the same line as times variable times is. 
	 * if times is small or equal than 0 than error message will be printed
	 */
	public static void printXChars(int times, char ch)
	{
		if(times >= 0)
		{
			for(int i=0;i<times;i++)
			{
				System.out.print(ch);
			}
		}
		else
		{
			System.out.println("ERROR TIMES IS NOT POSTIVE");
		}
		System.out.println();
	}
	public static void printXChars(int times)
	{
		printXChars(times,'*');
	}
	public static void main(String[] args) 
	{
		printXChars(4);
	}

}
