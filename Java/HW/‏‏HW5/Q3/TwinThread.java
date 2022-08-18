
public class TwinThread extends Thread
{
	private int N;
	
	public TwinThread(int N)
	{
		this.N = N;
	}
	
	@Override
	public void run()
	{
		checkIfTwins();
	}
	
	public void checkIfTwins()
	{
		int num1 = (int) (Math.random()*N);
		int num2 = (int) (Math.random()*N);
		if(calculateSumOfDigits(num1) == calculateSumOfDigits(num2))
		{
			System.out.printf("%d\t%d - ARE TWINS", num1, num2);
		}
	}
	
	public int calculateSumOfDigits(int num)
	{
		int sum = 0;
		while(num != 0)
		{
			sum += num % 10;
			num = num / 10;
		}
		return sum;
	}
}
