
public class PlasticBox extends Box
{
	private boolean liquidProof;
	private static final int BOXTYPESERIAL = 2;

	public PlasticBox(double volume, boolean liquidProof) {
		super(BOXTYPESERIAL, volume);
		this.liquidProof = liquidProof;
	}
	public boolean getRecyclable()
	{
		return false;
	}
	@Override
	public String toString() {
		return "The type of the box is PlasticBox. " + super.toString() + (this.liquidProof == true ? " The product is liquid proof" : "The product isn't liquid proof");
	}
	public boolean isLiquidProof() {
		return liquidProof;
	}
	
	 

}
