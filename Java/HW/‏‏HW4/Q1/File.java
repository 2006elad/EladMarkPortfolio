
public class File 
{
	private String name;
	private int bytes;
	public File(String name, int bytes) 
	{
		this.name = name;
		this.bytes = bytes;
	}
	public File(File other)
	{
		this(other.name, other.bytes);
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public int getBytes() {
		return bytes;
	}
	public void setBytes(int bytes) {
		this.bytes = bytes;
	}
	@Override
	public String toString() {
		String string = String.format("The file name is: %s, the size of the file is: %s", this.getName(), this.getBytes());
		return string;	
	}

	@Override
	public boolean equals(Object other) {
		if(getClass() == other.getClass())
		{
			File file = (File) other;
			if((file.name == this.name) && (file.bytes == this.bytes))
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
	
}
