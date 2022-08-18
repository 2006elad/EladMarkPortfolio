package ex11;

public class Photo implements Enlargeable, Drawable
{
	private int height;
	private int width;
	private String content;
	
	public Photo(int height, int width, String content) {
		this.height = height;
		this.width = width;
		this.content = content;
	}

	public void draw() 
	{
		int len = content.length();
		
		for (int i = 0; i < len; i += width) 
		{
			System.out.println(content.substring(i, i + width));
		}
	}
	
	public void enlarge(int x)
	{
		String s = "";
		for (int i = 0; i < width; i++) {
			s += "*";
		}
		String frame = "";
		for (int i = 0; i < x; i++) 
			frame += s;

		content = frame + content + frame;
		height += 2 * x;
	}

	public void abc() {
		System.out.println("P");
	}

	
	
}
