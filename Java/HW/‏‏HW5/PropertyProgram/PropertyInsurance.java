//Lior hazoom 205972078	
// Elad mark 316293638

public interface PropertyInsurance 
{
	public static final int InsuranceMeterPrice = 8;
	
	/**
	 * Function that calculate property insurance price
	 * @return calculated tax price
	 */
	public double calcInsurance();
	
	/**
	 * Function how much insurance user need to pay 
	 * @param AmountOfDamage - amount of damage
	 * @return the final calculated cost
	 */
	public double insuranceClaim(int AmountOfDamage);
}
