package ex4;

public class RealNum 
{
	int intNum;
	double remainder;
	public int getIntNum() {
		return intNum;
	}
	public void setIntNum(int intNum) {
		this.intNum = intNum;
	}
	public double getRemainder() {
		return remainder;
	}
	public void setRemainder(double remainder) {
		this.remainder = remainder;
	}
	public double getFullNum()
	{
		return this.intNum + this.remainder;
	}
	public int samePart(double num)
	{
		int intNum = (int)num;
		double reminder = num % intNum;
		if((intNum == this.intNum && reminder != this.remainder) || (intNum != this.intNum && reminder == this.remainder))
		{
			return 1;
		}
		else if(intNum == this.intNum && reminder == this.remainder)
		{
			return 2;
		}
		else
		{
			return 0;
		}
	}
}
