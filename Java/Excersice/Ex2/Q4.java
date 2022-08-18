package ex2;
import java.util.*;

public class Q4 
{
	/*
	 * 
	 */
	public static ArrayList<String> notInA2(ArrayList<String> a1, ArrayList<String> a2)
	{
		ArrayList<String> a3 = new ArrayList<String>();
		for(String str : a1)
		{
			if(!a2.contains(str) && !a3.contains(str))
			{
				a3.add(str);
			}
			
		}
		return a3;
		
	}
	public static void main(String[] args) 
	{
		ArrayList<String>  a1 = new ArrayList<String>();
		a1.add("AM");
		a1.add("AN");
		a1.add("SR");
		a1.add("AN");
		ArrayList<String>  a2 = new ArrayList<String>();
		a2.add("AM");
		a2.add("DR");
		a2.add("HV");
		a2.add("abc");
		System.out.println(notInA2(a1,a2));
	}

}
