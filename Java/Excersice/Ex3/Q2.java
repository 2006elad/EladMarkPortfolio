package ex3;

public class Q2 
{
	/**
	 * 
	 * @param num - the num we want to check his digits
	 * @param even - boolean that tell if we want to count the even or odd
	 * @return - function return count - that count the digits as the rule of even variable
	 */
	public static int countDigits(int num, boolean even)
	{
		num = Math.abs(num);
		int count = 0;
//		if(even == true)
//		{
//			while(num !=0)
//			{
//				if(num % 2 == 0)
//				{
//					count++;
//				}
//				num = num / 10;
//			}
//		}
//		else
//		{
//			while(num !=0)
//			{
//				if(num % 2 != 0)
//				{
//					count++;
//				}
//				num = num / 10;
//			}
//		}
		while(num > 0)
		{
			int digit = num % 10;
			boolean digitIsEven = digit % 2 == 0;
			if(even && digitIsEven)
			{
				count++;
			}
			else if(!even && !digitIsEven)
			{
				count++;
			}
			num = num / 10;
		}
		return count;
	}
	public static void main(String[] args) 
	{
		System.out.println(countDigits(4102,true));
	}

}
