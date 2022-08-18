
import java.util.ArrayList;

public class ClosedQuestion extends Question {

	private boolean singleOption;
	private ArrayList<String> allOptions;
	private ArrayList<String> isCorrect;

	public ClosedQuestion(int id, String title, boolean mandatory, boolean singleOption) {
		super(id, title, mandatory);
		this.singleOption = singleOption;

		allOptions = new ArrayList<>();
		isCorrect = new ArrayList<>();
	}

	public ClosedQuestion(ClosedQuestion otherClosedQuestion) {

		super(otherClosedQuestion);
		singleOption = otherClosedQuestion.singleOption;

		allOptions = new ArrayList<>(otherClosedQuestion.allOptions);
		isCorrect = new ArrayList<>(otherClosedQuestion.isCorrect);

		
	}

	public boolean isSingleOption() {
		return singleOption;
	}

	public void setSingleOption(boolean singleOption) {
		if(singleOption && !this.singleOption)
		{
			int i = 0;
			boolean first = true;
			
			while(i < isCorrect.size() && first)
			{
				if(isCorrect.get(i).equals("T"))					
					first = false;
				
				i++;
			}
			
			while(i < isCorrect.size())
			{
				if(isCorrect.get(i).equals("T"))					
					isCorrect.set(i, "F");
				i++;				
			}
		}
		this.singleOption = singleOption;
	}

	public void addOption(String option, boolean correct) {
		allOptions.add(option);

		if (correct) {
			isCorrect.add("T");
		} else {
			isCorrect.add("F");
		}
	}

	@Override
	public boolean checkReply(ArrayList<String> answer) {

		boolean correct = true;
		int index = 0;
		for (String option : answer) {
			int i = allOptions.indexOf(option);
			if(i == -1)
				return false;
			
			if(isCorrect.get(i).equals("F"))
				return false;
		}
		return true;
	}

	@Override
	public void show() {
		super.show();
		String string = null;
		if(this.singleOption)
		{
			string = "has a single correct option";
		}
		else
		{
			string = "has several correct options";
		}
		System.out.println(string);

		for(int i=0;i<this.allOptions.size();i++)
		{

			System.out.printf("['%s'] %s\n", this.isCorrect.get(i), this.allOptions.get(i));
		}
	}
	

}
