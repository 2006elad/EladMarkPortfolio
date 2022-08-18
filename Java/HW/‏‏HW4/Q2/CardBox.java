
public class CardBox extends Box
{
	private boolean liquidProof;
	private static final int BOXTYPESERIAL = 1;

	public CardBox(double volume, boolean liquidProof) {
		super(BOXTYPESERIAL, volume);
		this.liquidProof = liquidProof;
	}
	
	
	public boolean isLiquidProof() {
		return liquidProof;
	}


	public boolean getRecyclable()
	{
		return true;
	}
	@Override
	public String toString() {
		return "The type of the box is CardBox. " + super.toString() + (this.liquidProof == true ? " The product is liquid proof" : " The product isn't liquid proof");
	}
	
	 

}
