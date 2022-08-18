import java.util.ArrayList;

public class T8 {

	public static void main(String[] args) 
	{
		Question q1 = new Question(1, "Write your favourite country’s name", false);
//		 q1.show();
		OpenQuestion q2 = new OpenQuestion(2, "Write About you last vacation", true, true);
//		q2.show();
		ClosedQuestion q3 = new ClosedQuestion(3, "Mark european capital cities", false, false);
		q3.addOption("Jerusalem", false);
		q3.addOption("Barcelona", false);
		q3.addOption("Paris", true);
		q3.addOption("Madrid", true);
//		q3.show();
		
		ArrayList<Question> questions = new ArrayList<Question>();
		questions.add(q1);
		questions.add(q2);
		questions.add(q3);
		ArrayList<String> answer1 = new ArrayList<String>();
		answer1.add("Paris");
		answer1.add("Barcelona");
		ArrayList<String> answer2 = new ArrayList<String>();
		answer2.add("Paris");
		answer2.add("Madrid");
		for(int i = 0; i< questions.size(); i++)
		{
			System.out.println(questions.get(i).checkReply(answer1));
			System.out.println(questions.get(i).checkReply(answer2));
		}

	}

}
