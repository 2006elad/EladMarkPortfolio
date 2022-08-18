package ex7;

import java.util.ArrayList;

public class CloseQuestion extends Question
{
	private boolean singleOption;
	private ArrayList<String> allOptions;
	private ArrayList<String> isCorrect;
	public CloseQuestion(int id, String title, boolean mandatory, boolean singleOption) {
		super(id, title, mandatory);
		this.singleOption = singleOption;
		this.allOptions = new ArrayList<String>();
		this.isCorrect = new ArrayList<String>();
	}

	public CloseQuestion(CloseQuestion other) 
	{
		super(other);
		this.singleOption = other.singleOption;
		this.allOptions = new ArrayList<String>(other.allOptions);
		this.isCorrect = new ArrayList<String>(other.isCorrect);
	}

	public boolean isSingleOption() {
		return singleOption;
	}

	public void setSingleOption(boolean singleOption) 
	{
		if(!this.singleOption && singleOption)
		{
			this.singleOption = singleOption;
			boolean tFound = false;
			for(int i=0; i<this.isCorrect.size();i++)
			{
				if(tFound == true)
				{
					this.isCorrect.set(i, "F");			
				}
				else
					if(this.isCorrect.get(i).equals( "T"))
					{
						tFound = true;
					}
				
			}
		}
	}
	public void addOption(String option, boolean correct)
	{
		if(correct == true)
		{
			this.allOptions.add(option);
			this.isCorrect.add("T");
		}
		else
		{
			this.allOptions.add(option);
			this.isCorrect.add("F");

		}
	}
	private int returnAnswerIndex(String oneAnswer)
	{
		for(int i=0;i<this.allOptions.size();i++)
		{
			if(this.allOptions.get(i).equals(oneAnswer))
			{
				return i;
			}
		}
	}
	
	public boolean checkReply(ArrayList<String> answer)
	{
		for(int i=0;i<answer.size();i++)
		{
			if(this.allOptions.get())
		}
	}

}
