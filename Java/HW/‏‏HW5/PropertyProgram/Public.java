//Lior hazoom 205972078	
// Elad mark 316293638

public class Public extends Property  implements PropertyInsurance, PropertyTaxes
{
	private String type;

	public Public(String street, int number, int apt, int size, String type , String ownerName, String ownerId, int ownerNumber) throws Exception
	{
		super(street, number, apt, size , ownerName, ownerId, ownerNumber);
		this.type = type;
	}

	@Override
	public String toString() {
		return "~~~Property Details~~~\nThe type of the property is " + this.type + super.toString();
	}
	
	public String getType() {
		return type;
	}

	public void setType(String type) {
		this.type = type;
	}

	@Override
	public double calcPropertyTax() {
		return this.getSize() * 22;
	}

	@Override
	public void ownershipTransfer(String name, String id, int phone) {
		
	}

	@Override
	public void ownershipDetails() {
		// TODO Auto-generated method stub
		
	}

	@Override
	public double calcInsurance() {
		return this.getSize() * 22;
	}

	@Override
	public double insuranceClaim(int AmountOfDamage) {
		return Math.max(AmountOfDamage, 0.6 * this.calcInsurance());
	}
}
