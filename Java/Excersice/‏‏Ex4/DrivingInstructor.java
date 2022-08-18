package ex4;

public class DrivingInstructor 
{
	private String name;
	private double price;
	private boolean isAutomatic;
	
	public double getPrice()
	{
		return price;
	}
	
	public void setPrice(double price)
	{
		this.price = price;
	}
	
	public String getName() 
	{
		return name;
	}

	public void setName(String name) 
	{
		this.name = name;
	}

	public boolean isAutomatic() 
	{
		return isAutomatic;
	}

	public void setAutomatic(boolean isAutomatic) 
	{
		this.isAutomatic = isAutomatic;
	}

	public boolean withinPrice(double budget, int lessons)
	{
		if(lessons * this.price > budget)
		{
			return false;
		}
		else
		{
			return true;
		}
	}
}
