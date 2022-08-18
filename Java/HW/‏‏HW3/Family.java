import java.util.ArrayList;

/**
 * Method the represent family gym subscription
 *
 */
public class Family extends Advanced 
{
	private int adult;
	private int kids;
	public Family(int monthlyCost, int month, int adult, int kids) {
		super(monthlyCost, month);
		this.adult = adult;
		this.kids = kids;
	}
	
	public int getAdult() {
		return adult;
	}
	/**
	 * Method that set num of adult. Num of adult must be bigger or equal to 1, otherwise - we put 1 as default
	 * @param adult
	 */
	public void setAdult(int adult) {
		if(adult < 1)
		{
			System.out.println("The minimum of adults is 1, adult value setted to 1");
			this.adult = 1;
		}
		else
		{
			this.adult = adult;
		}
	}
	
	public int getKids() {
		return kids;
	}
	
	/**
	 * Method that set num of kids. Num of kids must be bigger or equal to 0, otherwise - we put 0 as default
	 * @param kids
	 */
	public void setKids(int kids) 
	{
		if(kids < 1)
		{
			System.out.println("You can put only postive number than bigger and equal to 0, kids value setted to 0");
			this.kids = 0;
		}
		else
		{
			this.kids = kids;
		}
	}
	
	/**
	 * Override Method that calculate all of the family subscription price with their services
	 */
	public int calcCost()
	{
		int sumOfCost = super.calcCost();
		int yearPriceWithoutServices = super.calcCost() - (this.calcServicesCost(false) * 12);

		sumOfCost += ((this.getAdult() - 1) * (0.8 * yearPriceWithoutServices));
		sumOfCost += (this.getKids() * (0.6 * yearPriceWithoutServices));
		
		return sumOfCost;
	}
	
	/**
	 * Override Method that calculate the total refund of a family
	 */
	public int calcRefund(int untilMonth)
	{
		int sumOfRefund = super.calcRefund(untilMonth);
		int onePersonRefundWithoutServices = super.calcRefund(untilMonth) - (this.calcServicesCost(true) * this.calcNumOfMonthsToRefund(untilMonth));
		
		if(this.adult > 1)
		{
			sumOfRefund += 0.75 * onePersonRefundWithoutServices;
		}
		
		for(int i = 0; i < (this.kids + (this.adult -2)) ;i++)
		{
				sumOfRefund += 0.5 * onePersonRefundWithoutServices;
		}
		
		return sumOfRefund;
	}
	
	/**
	 * Override method that add to print methods the num of adult and kids in a family
	 */
	public void print()
	{
		super.print();
		System.out.printf("adults:<%s>, kids:<%s>\n", this.adult, this.kids);
	}
	

}
