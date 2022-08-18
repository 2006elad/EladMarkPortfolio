

import java.util.ArrayList;

public class Question {
	protected int id;
	protected String title;
	protected boolean mandatory;

	public Question(int id, String title, boolean mandatory) {

		this.id = id;
		this.title = title;
		this.mandatory = mandatory;
	}

	public Question(Question otherQuestion) {

		this.id = otherQuestion.id;
		this.title = otherQuestion.title;
		this.mandatory = otherQuestion.mandatory;
	}

	final public int getId() {
		return id;
	}

	final public void setId(int id) {
		this.id = id;
	}

	final public boolean isMandatory() {
		return mandatory;
	}

	final public void setMandatory(boolean mandatory) {
		this.mandatory = mandatory;
	}
	
	
	public String getTitle() {
		return title;
	}

	public void setTitle(String title) {
		this.title = title;
	}
	
	public void show()
	{
		String mandatory;
		if(isMandatory())
		{
			mandatory   = " (mandatory)";
		}
		else
		{
			mandatory  = " (not mandatory)";
		}
		System.out.print(id +". " + title + mandatory);
	}
	
	
	
	
	public boolean checkReply(ArrayList<String> answer)
	{
		return true;
	}

}
