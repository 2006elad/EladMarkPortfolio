
public class Q4 
{
	/**
	 * Sub withoutMajority Function that find in a string the majority char by using boyer-moore majority vote algorithem.
	 * @param str - the string we check. in the string there is one char that appears more than 50%
	 * @return - the majority char
	 */
	public static char majorityChar(String str)
	{
		int counter = 0, i;
		char m = 0;
//		while(i<str.length())
//		{
//			if(counter == 0)
//			{
//				m = str.charAt(i);
//				counter++;
//				i++;
//			}
//			else
//			{
//				if(str.charAt(i) == m)
//				{
//					counter++;
//					i++;
//				}
//				else
//				{
//					counter--;
//				}
//			}
//		}
		for(i=0; i<str.length();i++)
		{
			if(counter == 0)
			{
				m = str.charAt(i);
				counter++;
			}
			else
			{
				if(str.charAt(i) == m)
				{
					counter++;
				}
				else
				{
					counter--;
				}
			}
		}
		return m;
	}
	
	/**
	 * Function that using majorityChar function to find in a string the majority char.
	 * Then the function create new string without the char and return it the user.
	 * @param str - the string we checking and creating from the new string without the majority char
	 * @return - the new String without the majority char
	 */
	public static String withoutMajority(String str)
	{
		char majChar = majorityChar(str);
		String newStr = "";
		for(int i = 0; i < str.length(); i++)
		{
			if(str.charAt(i) != majChar)
			{
				newStr += str.charAt(i);
			}
		}
		return newStr;
	}
	public static void main(String[] args) 
	{
		String str = "abaaxakadsa";
		System.out.println(withoutMajority(str));
	}

}
