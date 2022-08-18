/**
 * Class that represent a gym service
 */
public class Service 
{
	private String serviceName;
	private int serviceMontlyCost;
	private boolean refundable;
	public Service(String serviceName, int serviceMontlyCost, boolean refundable) {
		super();
		this.serviceName = serviceName;
		this.serviceMontlyCost = serviceMontlyCost;
		this.refundable = refundable;
	}
	
	public Service(String serviceName, int serviceMontlyCost) 
	{
		this(serviceName, serviceMontlyCost, false);
	}
	/**
	 * Default constractor when month cost aren't given (default price is 10)
	 * @param serviceName - The Service we want to initilize
	 */
	public Service(String serviceName) 
	{
		this(serviceName, 10, false);
	}
	
	public Service(Service s) 
	{
		this(s.serviceName, s.serviceMontlyCost, s.refundable);
	}
	
	public String getServiceName() {
		return serviceName;
	}
	
	public int getServiceMontlyCost() {
		return serviceMontlyCost;
	}
	/**
	 * Method that set the service monthly cost. when the price that inputed is lower than 10 than the price is changed to default(10) 
	 * @param serviceMontlyCost - the service price we want to set
	 */
	public void setServiceMontlyCost(int serviceMontlyCost) {
		if(serviceMontlyCost < 10)
			{
				System.out.println("Service cost was lower than the minimum(10 Nis), Price updated to minimum");
				this.serviceMontlyCost = 10;
			}
	}
	public boolean isRefundable() {
		return refundable;
	}
	/**
	 * Method that print object of an service details
	 */
	public void print()
	{
		System.out.printf("serviceName:<%s>, serviceMonthlyCost:<%s>, refundable:<%s>\n",this.serviceName, this.serviceMontlyCost, this.refundable);
	}
}
