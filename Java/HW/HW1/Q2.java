import java.util.*;

public class Q2 
{
	/* Program for bucket company that count how much bucket with specific size (from 5-50, in 5 liter jump) is manufactured
	 * In the end printing the most manufactured size.
	 */
	public static void main(String[] args) 
	{
		
		Scanner input = new Scanner(System.in);
		int n;
		System.out.println("Please insert the amount of buckets you want to insert: ");
		n = input.nextInt();
		int bucket[] = new int[n];
		int countArr[] = new int[10];
		for(int i = 0; i<n; i++)
		{
			System.out.println("Please insert the capacity of bucket number " + (i+1) + " :");	
			bucket[i] = input.nextInt();
			boolean isValid = false;
			while(isValid != true)
			{
				if(bucket[i] % 5 ==0)
				{
					isValid = true;
				}
				else
				{
					System.out.println("You didn't insert valid capacity, Please insert again!");
					System.out.println("Please insert the capacity of bucket number " + (i+1) + " :");	
					bucket[i] = input.nextInt();
				}
			}
			countArr[bucket[i]/5 -1]++;
		}
		
		int max = 0;
		for(int i = 1; i < countArr.length; i++)
		{
			if(countArr[i] > max)
			{
				max = i;
			}
		}
		System.out.println((max + 1) * 5);
	}

}
