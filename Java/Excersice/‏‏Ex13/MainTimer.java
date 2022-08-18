import java.util.*;
public class MainTimer {

	public static void main(String[] args) 
	{
		Scanner input = new Scanner(System.in);
		Timer t = new Timer();
		t.start();
		boolean isFinish = false;
		while(!isFinish)
		{
			System.out.println("Insert 0 for stop the timer, insert 1 to print clock time");
			int choice = input.nextInt();
			if(choice == 1)
			{
				t.show();
			}
			else
			{
				if(choice == 0)
				{
					t.stopTimer();
					isFinish = true;
				}
			}
		}
		input.close();
	}

}
