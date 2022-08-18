package ex2;
import java.util.*;
public class Q3 
{
	public static void main(String[] args) 
	{
		Scanner input = new Scanner(System.in);
		int x, y;
		System.out.println("Input X");
		x = input.nextInt();
		System.out.println("Input Y");
		y = input.nextInt();	
		int seqArr[] = new int[x/y * 2];
		int val=0;
		for(int i = 0, j = seqArr.length -1; i < j; i++, j--)
		{
			val += y;
			seqArr[i] = val;
			seqArr[j] = val;
		}
		for(int i=0;i<seqArr.length;i++)
		{
			System.out.print(seqArr[i]);
		}
	}
}
