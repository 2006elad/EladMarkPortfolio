package ex11;

public class Triangle extends Polygon {

	private boolean spacing;
	public Triangle(int height, char filling, boolean spacing) {
		super(height, filling);
		this.spacing = spacing;
	}
	@Override
	public void draw() 
	{
		String f = "" + filling;
		if(spacing)
			f += " ";
		for (int i = 1; i <= height; i++) {
			for (int j = 1; j <= i; j++) {
				System.out.print(f);
			}
			System.out.println();
		}

	}
	public void abc() {
		System.out.println("T");
	}
}
