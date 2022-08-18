//Lior hazoom 205972078	
// Elad mark 316293638

public class Residential extends Property implements PropertyTaxes
{
	private int householdSize;
	public Residential(String street, int number, int apt, int size, int householdSize, String ownerName, String ownerId, int ownerNumber) throws Exception{
		super(street, number, apt, size, ownerName, ownerId, ownerNumber);
		if(householdSize < 0)
		{
			throw new Exception("House hold size Must be postive");
		}
		else
		{
			this.householdSize = householdSize;
		}
	}

	@Override
	public String toString() {
		return "~~~Property Details~~~\n" + super.toString() + "\nThe house hold Size: " + this.householdSize;
	}
	
	public int getHouseholdSize() {
		return householdSize;
	}

	public void setHouseholdSize(int householdSize) {
		this.householdSize = householdSize;
	}

	@Override
	public double calcPropertyTax() {
		double taxToPay = PropertyTaxes.TaxMeterPrice * this.getSize();
		if(this.householdSize >= 6)
		{
			return taxToPay * 0.85;
		}
		else
		{
			return taxToPay;
		}
	}

	@Override
	public void ownershipTransfer(String name, String id, int phone) {
		// TODO Auto-generated method stub
		
	}

	@Override
	public void ownershipDetails() {
		// TODO Auto-generated method stub
		
	}
}