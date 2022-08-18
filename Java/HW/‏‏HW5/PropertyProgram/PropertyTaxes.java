//Lior hazoom 205972078	
// Elad mark 316293638

public interface PropertyTaxes 
{
	public static final int TaxMeterPrice = 12;
	
	/**
	 * Function that calculate property taxes 
	 * @return final taxes cost
	 */
	public double calcPropertyTax();
	
	/**
	 * Function that transfer ownership of property
	 * @param name - name of the owner
	 * @param id - id of owner
	 * @param phone - number of owner
	 */
	public void ownershipTransfer(String name, String id, int phone);
	
	/**
	 * Function that print owner details
	 */
	public void ownershipDetails();
}
