package ex11;

public abstract class Polygon implements Drawable {

	protected int height;
	protected char filling;
	
	public Polygon(int height, char filling) 
	{
		this.height = height;
		this.filling = filling;
	}
	
	public abstract void draw();
}
