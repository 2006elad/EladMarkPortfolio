package ex10Q2;

public abstract class Software 
{
	private String name;
	private boolean isRunning;
	public Software(String name, boolean isRunning) {
		super();
		this.name = name;
		this.isRunning = isRunning;
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public boolean isRunning() {
		return isRunning;
	}
	public void setRunning(boolean isRunning) {
		this.isRunning = isRunning;
	}
	public boolean start()
	{
		if(this.isRunning)
		{
			System.out.println("The software is already running!");
			return false;
		}
		else
		{
			this.isRunning = true;
			return true;
		}
	}	
	public abstract boolean stop();
	
}
