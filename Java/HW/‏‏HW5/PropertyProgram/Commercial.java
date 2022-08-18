//Lior hazoom 205972078	
// Elad mark 316293638

public class Commercial extends Property implements PropertyTaxes, PropertyInsurance
{
	private char smb;
	public Commercial(String street, int number, int apt, int size, char smb , String ownerName, String ownerId, int ownerNumber) throws Exception {
		super(street, number, apt, size , ownerName, ownerId, ownerNumber);
		smb = java.lang.Character.toUpperCase(smb);
		if(smb =='L' || smb == 'M' || smb == 'S')
		{
			this.smb = smb;
		}
		else
		{
			throw new Exception("You can only enter The letter L, M or S");
		}
	}
	
	public char getSmb() {
		return smb;
	}

	public void setSmb(char smb) {
		this.smb = smb;
	}

	@Override
	public double calcPropertyTax() {
		double updatedMeterPrice;
		if(smb == 'S')
		{
			updatedMeterPrice = PropertyTaxes.TaxMeterPrice * 1.6;
		}
		else if(smb == 'M')
		{
			updatedMeterPrice = PropertyTaxes.TaxMeterPrice * 2;
		}
		else
		{
			updatedMeterPrice = PropertyTaxes.TaxMeterPrice * 2.4;
		}
		return this.getSize() * updatedMeterPrice;
	}
	@Override
	public void ownershipTransfer(String name, String id, int phone) {
			super.setOwnerName(name);
			super.setOwnerId(id);
			super.setOwnerNumber(phone);
	}
	@Override
	public void ownershipDetails() {
		String.format("The owner Name is:%s, His id is: %s, his phone number is:%s\n", this.getOwnerName(), this.getOwnerId(), this.getOwnerNumber());
	}
	
	@Override
	public double calcInsurance() {
		double updatedMeterPrice;
		if(smb == 'S')
		{
			updatedMeterPrice = PropertyInsurance.InsuranceMeterPrice + 10;
		}
		else if(smb == 'M')
		{
			updatedMeterPrice = PropertyInsurance.InsuranceMeterPrice + 15;
		}
		else
		{
			updatedMeterPrice = PropertyInsurance.InsuranceMeterPrice + 20;
		}
		return this.getSize() * updatedMeterPrice;
	}

	@Override
	public double insuranceClaim(int AmountOfDamage) {
		double insuranceAndDamageDiff = this.calcInsurance() - AmountOfDamage;
		if(insuranceAndDamageDiff <= 0)
		{
			return 0;
		}
		else
		{
			return insuranceAndDamageDiff;
		}
	}

	public String toString() {
		return "~~~Property Details~~~\nThe Size of the commerical is: " + this.smb + "\n" + super.toString();
	}
	

}
