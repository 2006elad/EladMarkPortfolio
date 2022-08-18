package ex11;

public class Rectangle extends Polygon implements Enlargeable, Reducible{

	private int width;
	
	public Rectangle(int height, char filling, int width) {
		super(height, filling);
		this.width = width;
	}

	@Override
	public void reduce(int x)
	{
		this.height -=x;
		this.width -=x;
	}

	@Override
	public void enlarge(int x) 
	{
		this.height +=x;
		this.width +=x;
	}

	@Override
	public void draw() 
	{
		for (int i = 0; i < height; i++) 
		{
			for (int j = 0; j < width; j++) {
				System.out.print(filling);				
			}
			System.out.println();
		}
	}

	public void abc() {
		System.out.println("R");
	}
	

}