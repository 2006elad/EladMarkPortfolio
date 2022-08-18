package ex4;

public class Car 
{
	private String companyName;
	private double maxSpeed;
	private double currentSpeed;
	
	public void accelerate(double rate)
	{
		double new_speed = this.currentSpeed * rate;
		if(this.currentSpeed == 0)
		{
			this.currentSpeed = rate;
		}
		else if(new_speed > this.maxSpeed)
		{
			this.currentSpeed = this.maxSpeed;
		}
		else
		{
			this.currentSpeed = new_speed;
		}
	}

	public String getCompanyName() 
	{
		return companyName;
	}

	public void setCompanyName(String companyName) 
	{
		this.companyName = companyName;
	}

	public double getMaxSpeed() 
	{
		return maxSpeed;
	}

	public void setMaxSpeed(double maxSpeed) 
	{
		if(maxSpeed < 100)
		{
			this.maxSpeed = 100;
		}
		else
		{
			this.maxSpeed = maxSpeed;
		}
	}

	public double getCurrentSpeed() 
	{
		return currentSpeed;
	}

	public void setCurrentSpeed(double currentSpeed) {
		if(currentSpeed < 0)
		{
			this.currentSpeed = 0;
		}
		else
		{
			this.currentSpeed = currentSpeed;
		}
	}
}
