/*
 * 
 * Class That represent a basic subscribe of a gym
 */
public class Subscriber	
{
	private int monthlyCost;
	private int month;
	
	public Subscriber(int monthlyCost, int month) {
		super();
		this.monthlyCost = monthlyCost;
		this.month = month;
	}
	
	public int getMonthlyCost() {
		return monthlyCost;
	}
	
	/**
	 * Method that set the monthly cost by the rules(minimum price is 100)
	 * @param monthlyCost - subscriber month cost
	 */
	public void setMonthlyCost(int monthlyCost) {
		if(monthlyCost < 100)
		{
			System.out.println("Service cost was lower than the minimum(10 Nis), Price updated to minimum");
			this.monthlyCost = 100;
		}
	}
	
	public int getMonth() {
		return month;
	}
	
	/**
	 * Method that calculate total price of a year
	 * @return - the calculated price (integer)
	 */
	public int calcCost()
	{
		return this.monthlyCost * 12;
	}
	
	/**
	 * Method that calculate and return the refund that user need to get by the month his leaving 
	 * @param untilMonth - the month subscriber stop the subscribe
	 * @return - the calculated refund in integer
	 */
	public int calcRefund(int untilMonth)
	{
		return this.monthlyCost * this.calcNumOfMonthsToRefund(untilMonth);
	}
	
	/**
	 * Method that print Subscriber class details
	 */
	public void print()
	{
		System.out.printf("monthlyCost:<%s>, month:<%s>\n", this.monthlyCost, this.month);
	}
	
	/**
	 * Help function that find how many months are need to be refunded.
	 * @param untilMonth - the month that subscriber stop the subscribe
	 * @return - the number of months to refund
	 */
	public int calcNumOfMonthsToRefund(int untilMonth)
	{
		int curMonthNum = this.month;
		int count = 0;
		while(curMonthNum != untilMonth)
		{
			if(curMonthNum == 12)
			{
				curMonthNum = 1;
			}
			else
			{
				curMonthNum++;
			}
			count++;
		}
		return (12 - count);
	}
		
}
