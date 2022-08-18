package ex3;

public class Q3 
{
	/**
	 * Function that check that all chars in string is not equal(lower or upper case)
	 * @param str - string we want to check
	 * @return true - true if unique else false
	 */
	public static boolean uniqueChars(String str)
	{
		boolean isUnique = true;
		int i = 0;
		while(i<str.length() -1 && isUnique)
		{
			String ch = String.valueOf(str.charAt(i)).toLowerCase();
			boolean beforeSubString = str.substring(0, i).contains(ch);
			boolean afterSubString = str.substring(i+1, str.length()).contains(ch);
			if(beforeSubString || afterSubString)
			{
				isUnique = false;
			}
			else
			{
				i++;
			}
		}
		return isUnique;
	}
	public static void main(String[] args) 
	{
		System.out.println(uniqueChars("AbC"));
	}

}
