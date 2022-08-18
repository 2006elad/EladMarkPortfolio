public class Q3 
{
	/**
	 * isZigzag sub function that change replace indexes each two values
	 * @param arr - the array we want to change
	 * @return - None
	 */
	public static void zigZag(int arr[])
	{
		int temp;
		for(int i = 0; i<arr.length; i+=2)
		{
			temp = arr[i];
			arr[i] = arr[i + 1];
			arr[i + 1] = temp;
		}
	}
	
	/**
	 * Function that Check two even array, if one array is the zigzag of the other one.
	 * @param arr - array 1
	 * @param brr - array 2
	 * @return - True if they are zigzag, False - if not.
	 */
	public static boolean isZigZag(int arr[], int brr[])
	{ 
		if(arr.length == brr.length)
		{		
			int brrCopy[] = brr.clone();
			zigZag(brrCopy);
			for(int i = 0; i<arr.length;i++)
			{
				if(arr[i] != brrCopy[i])
				{
					return false;
				}
			}
			return true;
		}
		else
		{
			return false;
		}
	}
	public static void main(String[] args) 
	{
		int arr[] = {5, 6, 3, 4, 1, 2};
		int brr[] = {6, 5, 4, 3, 2, 1};
		System.out.println(isZigZag(arr, brr));
		for(int i = 0; i<brr.length; i++)
		{
			System.out.println(brr[i]);
		}
		
	}

}
