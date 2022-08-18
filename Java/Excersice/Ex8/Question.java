
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

	public final int getId() {
		return id;
	}

	public final void setId(int id) {
		this.id = id;
	}

	public String getTitle() {
		return title;
	}

	public void setTitle(String title) {
		this.title = title;
	}

	public final boolean isMandatory() {
		return mandatory;
	}

	public final void setMandatory(boolean mandatory) {
		this.mandatory = mandatory;
	}
	
	public boolean checkReply(ArrayList<String> answer)
	{
		return true;
	}
	public void show()
	{
		String mandatory = null;
		if(this.mandatory == true)
		{
			mandatory = "(Mandatory)\n";
		}
		else
		{
			mandatory = "(not Mandatory)\n";
		}

		System.out.printf("%s. %s %s", this.id, this.title, mandatory);
	}
	

}
