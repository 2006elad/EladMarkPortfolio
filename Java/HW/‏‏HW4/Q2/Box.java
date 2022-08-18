

public abstract class Box 
{
	private int serialNum;
	private double volume;
	private static int counter = 0; 
	
	public Box(int BOXTYPESERIAL, double volume) {
		this.serialNum = (++counter * 10) + BOXTYPESERIAL;
		this.volume = volume;	
	}
	
	
	public abstract boolean getRecyclable();
	
	public int getSerialNum() {
		return serialNum;
	}


	public double getVolume() {
		return volume;
	}
	
	/**
	 * Method that we get from it the num of produced boxes in the company
	 * @return
	 */
	public static int getNumOfProducedProduct()
	{
		return counter;
	}
	
	public boolean equals(Object other)
	{
		if(getClass() == other.getClass())
		{
			Box box = (Box) other;
			if(box.serialNum == this.serialNum)
			{
				return true;
			}
			else
			{
				return false;
			}
		}
		else
		{
			return false;
		}
	}
	@Override
	public String toString() {
		String string = String.format("Box serial num is: %s, box volume is %s", this.serialNum, this.volume);
		return string;
	}
	
	
}
