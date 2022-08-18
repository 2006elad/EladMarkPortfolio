import java.util.*;
public class Main
{

	public static void main(String[] args) 
	{
		Scanner input = new Scanner(System.in);
		System.out.println("Insert N");
		int N = input.nextInt();

		TwinThread t1 = new TwinThread(N);
		TwinThread t2 = new TwinThread(N);
		TwinThread t3 = new TwinThread(N);


		for(int i=0;i<N;i++)
		{
			t1.start();
			t2.start();
			t3.start();
			while(t1.isAlive()||t2.isAlive()|t3.isAlive())
			{
			}
		}
		input.close();
	}

}
