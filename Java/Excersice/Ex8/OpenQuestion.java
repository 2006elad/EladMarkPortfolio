public final class OpenQuestion extends Question {

	private boolean singleLine;

	public OpenQuestion(int id, String title, boolean mandatory, boolean singleLine) {
		super(id, title, mandatory);
		this.singleLine = singleLine;
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

	@Override
	public void setTitle(String title) {
		title = "[OpenQ]" + title;
		super.setTitle(title);
	}
	@Override
	public void show() {
		// TODO Auto-generated method stub
		super.show();
		String singleTitle = null;
		if(this.singleLine)
		{
			singleTitle = "in a single line\n";
		}
		else
		{
			singleTitle = "in a several line\n";
		}
		System.out.println(singleTitle);
	}
	
	
}
