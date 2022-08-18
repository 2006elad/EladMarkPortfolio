package ex7;

public class OpenQuestion extends Question 
{
	private boolean singleLine;

	public OpenQuestion(int id, String title, boolean mandatory, boolean singleLine) {
		super(id, title, mandatory);
		this.singleLine = singleLine;
	}
	public OpenQuestion(OpenQuestion other) 
	{
		super(other);
		this.singleLine = other.singleLine;
	}
	public boolean isSingleLine() {
		return singleLine;
	}

	public void setSingleLine(boolean singleLine) {
		this.singleLine = singleLine;
	}
	
}
