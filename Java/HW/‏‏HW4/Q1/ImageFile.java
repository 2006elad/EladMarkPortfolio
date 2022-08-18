
public class ImageFile extends File
{
	private int width;
	private int height;
	public ImageFile(String name, int bytes, int width, int height) {
		super(name, bytes);
		this.width = width;
		this.height = height;
	}
	public ImageFile(ImageFile other)
	{
		super(other);
		this.width = other.width;
		this.height = other.height;
	}
	public int getWidth() {
		return width;
	}
	public void setWidth(int width) {
		this.width = width;
	}
	public int getHeight() {
		return height;
	}
	public void setHeight(int height) {
		this.height = height;
	}
	@Override
	public String toString() {
		String string = String.format("The file name is: %s, the size of the file is: %s. The Image Width is: %s, and the height is: %s.", this.getName(), this.getBytes(), this.width, this.height);
		return string;
	}
	@Override
	public boolean equals(Object other) {
		if(getClass() == other.getClass())
		{
			ImageFile imageFile = (ImageFile) other;
			if(super.equals(other) && (imageFile.width == this.width) && (imageFile.height == this.height))
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
