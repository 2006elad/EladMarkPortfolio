package ex7;

import java.util.ArrayList;

public class Question 
{
	private int id;
	private String title;
	private boolean mandatory;
	public Question(int id, String title, boolean mandatory) {
		this.id = id;
		this.title = title;
		this.mandatory = mandatory;
	}
	public Question(Question other) {
		this(other.id, other.title, other.mandatory);
	}
	public int getId() {
		return id;
	}
	public void setId(int id) {
		this.id = id;
	}
	public String getTitle() {
		return title;
	}
	public void setTitle(String title) {
		this.title = title;
	}
	public boolean isMandatory() {
		return mandatory;
	}
	public void setMandatory(boolean mandatory) {
		this.mandatory = mandatory;
	}
	public boolean checkReply(ArrayList<String> answer)
	{
		return true;
	}
}
