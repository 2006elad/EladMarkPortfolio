import java.util.Scanner;

public class Quiz extends Thread
{
	private boolean answerStatus = false;
	
	@Override
	public void run() 
	{
		presentQuiz();
	}
	
	public void presentQuiz()
	{
		Scanner in = new Scanner(System.in);
		int num1 = (int)(Math.random() * 1000);
		int num2 = (int)(Math.random() * 1000);
		System.out.println("How fast are you?");
		System.out.printf("[ %d + %d ] =", num1, num2);
		System.out.println();
		int ans = in.nextInt();
		answerStatus = true;//change property status after answer submission
		if(ans == num1 + num2)
			System.out.println("You're a winner");
		else
		    System.out.println("Wrong answer, try again next time");
		in.close();
	}
	
	public boolean getStatus()
	{
		return answerStatus;
	}
}
