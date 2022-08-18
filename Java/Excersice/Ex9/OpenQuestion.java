

public final class OpenQuestion extends Question {

	private boolean singleLine;

	
	
	@Override
	public void setTitle(String title) {
		
		super.setTitle("[OpenQ] " +title);
	}

	public OpenQuestion(int id, String title, boolean mandatory, boolean singleLine) {
		super(id, "[OpenQ] " +title, mandatory);
		this.singleLine = singleLine;
	}

	
	
	@Override
	public void show() {
		
		String singleLine;
		if(this.singleLine)
		{
			singleLine = " in a single line";
		}
		else
		{
			singleLine = " in several lines";
		}
		System.out.println();
		super.show();
		System.out.println(singleLine);
	}

	public OpenQuestion(OpenQuestion otherOpenQuestion) {
		super(otherOpenQuestion);

		this.singleLine = otherOpenQuestion.singleLine;
	}

	public boolean isSingleLine() {
		return singleLine;
	}

	public void setSingleLine(boolean singleLine) {
		this.singleLine = singleLine;
	}

}
