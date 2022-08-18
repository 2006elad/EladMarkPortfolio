//Lior hazoom 205972078	
// Elad mark 316293638

public abstract class Property
{

	private String street;
	private int number;
	private int apt;
	private int size;
	private String ownerName;
	private String ownerId;
	private int ownerNumber;
	public Property(String street, int number, int apt, int size, String ownerName, String ownerId, int ownerNumber) throws Exception
	{
		if(street.isEmpty())
		{
			throw new Exception("Street name is empty");
		}
		else
		{
			this.street = street;
		}
		if(number < 0)
		{
			throw new Exception("Home Number Must be postive");
		}
		else
		{
			this.number = number;
		}
		if(apt < 0)
		{
			throw new Exception("Apt Number Bigget or equal than 0");
		}
		else
		{
			this.apt = apt;
		}
		if(number < 0)
		{
			throw new Exception("Home size Must be postive");
		}
		else
		{
			this.size = size;
		}
		this.ownerName = ownerName;
		this.ownerId = ownerName;
		this.ownerNumber = ownerNumber;	
	}
	@Override
	public boolean equals(Object other) 
	{
		if(getClass() == other.getClass())
		{
			Property prop = (Property) other;
			if(prop.street.equals(this.street) && prop.number == this.number && prop.apt == this.apt)
			{
				return true;
			}
			else
			{
				return false;
			}
		}
		else
		{
			return false;
		}
	}
	@Override
	public String toString() {
			return String.format("Street Name: %s\nHouse Number:%s\nApartment Number:%s\nThe size is:%s", this.street, this.number, this.apt, this.size);
		}
	public int getSize() {
		return size;
	}
	public void setSize(int size) {
		this.size = size;
	}
	public String getStreet() {
		return street;
	}
	public int getNumber() {
		return number;
	}
	public int getApt() {
		return apt;
	}
	public String getOwnerName() {
		return ownerName;
	}
	public void setOwnerName(String ownerName) {
		this.ownerName = ownerName;
	}
	public String getOwnerId() {
		return ownerId;
	}
	public void setOwnerId(String ownerId) {
		this.ownerId = ownerId;
	}
	public int getOwnerNumber() {
		return ownerNumber;
	}
	public void setOwnerNumber(int ownerNumber) {
		this.ownerNumber = ownerNumber;
	}
	
}
