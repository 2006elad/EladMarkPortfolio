
public class Timer extends Thread
{
	private int m;
	private int s;
	private int h;
	private boolean working;
	public Timer() {
		super();
		this.s =0;
		this.m = 0;
		this.h = 0;
		this.working = false;
	}
	
	@Override
	public void run() 
	{
		this.working = true;
		System.out.println("working started Timer");
		while(this.working)
		{
			try {
				Thread.sleep(1000);
				s++;
				if(this.s == 60)
				{
					this.s = 0;
					this.m++;
					if(this.m == 60)
					{
						this.h++;
						if(this.h == 24)
						{
							this.h = 0;
						}
					}
				}
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
		System.out.println("Timer Stopped");	}
	
	public void stopTimer()
	{
		this.working = false;
	}
	
	public void show()
	{
		System.out.printf("%02d:%02d:%02d\n", this.h, this.m, this.s);
	}
	
	
}
