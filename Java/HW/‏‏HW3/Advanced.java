import java.util.ArrayList;

/**
 *	Class that represent advanced subscription
 */
public class Advanced extends Subscriber 
{
	private ArrayList<Service> services;

	public Advanced(int monthlyCost, int month) {
		super(monthlyCost, month);
		this.services = new ArrayList<Service>();
	}
	
	/**
	 * Add services cost to calculated subscription price 
	 */
	@Override 
	public int calcCost()
	{
		return super.calcCost() + (this.calcServicesCost(false) * 12);
	}
	
	/**
	 * Add the refundable services to the calculated refund
	 */
	public int calcRefund(int untilMonth)
	{
		return super.calcRefund(untilMonth) + (this.calcServicesCost(true) * super.calcNumOfMonthsToRefund(untilMonth));
	}
	
	/**
	 * Method that check if a service is found by name
	 * @param name - the name of the service we want to find
	 * @return true if found, false - if not
	 */
	public boolean serviceExist(String name)
	{
		for(int i=0; i<this.services.size(); i++)
		{
			if(this.services.get(i).getServiceName().equals(name))
			{
				return true;
			}
		}
		return false;
	}
	
	/**
	 * Method that add service to advanced subscribe - if service is already existed then a message printed to console 
	 * @param service - the service we want to add
	 */
	public void addService(Service service)
	{
		if(serviceExist(service.getServiceName()))
		{
			System.out.println("Service is already exist");
		}
		else
		{
			this.services.add(service);
		}
	}
	
	/**
	 *  Method that add to subscriber print, all of the services
	 */
	public void print()
	{
		super.print();
		for(int i=0; i<this.services.size(); i++)
		{
			this.services.get(i).print();
		}
	}
	
	/**
	 * Help method that calculate 1 month of total services price with or without refundable services
	 * @param onlyRefundable - True - when we want to calculate only the refundable services (for refund method), False - when to sum all of services
	 * @return - 1 month total sum price
	 */
	public int calcServicesCost(boolean onlyRefundable)
	{
		int sumOfServicesPrice = 0;
		if(onlyRefundable == true)
		{
			for(int i=0; i<this.services.size(); i++)
			{
				if(this.services.get(i).isRefundable() == true)
				{
					sumOfServicesPrice+= this.services.get(i).getServiceMontlyCost();
				}
			}
		}
		else
		{
			for(int i=0; i<this.services.size(); i++)
			{
				sumOfServicesPrice+= this.services.get(i).getServiceMontlyCost();
			}
		}
		return sumOfServicesPrice;
		
	}
}
