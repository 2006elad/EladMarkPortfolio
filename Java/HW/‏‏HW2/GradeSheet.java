/**
 * Class that represent one student grade sheet with the test he did in specfic course in each quarter
 * @author User
 *
 */
public class GradeSheet 
{
	private  String studentName;
	private Exam[][] exams;
	
	public GradeSheet(String studentName)
	{
		this.studentName = studentName;
		this.exams = new Exam[8][4];
	}
	/** Function that add one exam to the right course and right quarter in exams list
	 * @param e: the test we want to add
	 */
	public void addOneExam(Exam e)
	{
		if(this.exams[e.getCourse() -1 ][e.getQuarter() -1] == null)
		{
			this.exams[e.getCourse() -1][e.getQuarter() - 1] = new Exam(e);
		}
		else
		{
			if(this.exams[e.getCourse() - 1][e.getQuarter() - 1].getGrade() < e.getGrade())
			{
				this.exams[e.getCourse() - 1][e.getQuarter() - 1].setGrade(e.getGrade());
				System.out.println("Course Qurtuer test grade has been updated!");
			}
		}
			
	}
	/**
	 * Function that find and return the grade mean of a specific course by the rules user decided(mean all of the test with test student didn't did or the mean of the he did) 
	 * @param course - the course code of the course we want to find his mean
	 * @param all - if all true then we want to return the mean that include all the tests although if student didn't did a test, when all is false then we return the mean of tests student did  
	 * @return - the right mean in float
	 */
	public float calculateMean(int course, boolean all)
	{
		float sum = 0;
		if(all == true)
		{
			for(int i = 0; i < 4; i++)
			{
				sum += this.exams[course - 1][i].getGrade();
			}
			return sum / 4;
		}
		else
		{
			int count = 0;
			for(int i = 0; i < 4; i++)
			{
				if(this.exams[course - 1][i].getGrade() != -1)
				{
					count ++;
					sum += this.exams[course - 1][i].getGrade();
				}
			}
			if(count != 0)
			{
				return sum / count;
			}
			else
			{
				System.out.println("There aren't any test in this course");
				return 0;
			}
		}
	}
	/**
	 * Function that print the full student tests details(course name, quarter and grade) sheet only with the test he did
	 */
	public void Print()
	{
		System.out.println(this.studentName);
		
		String starsStr = "";
		for(int i = 0; i < this.studentName.length(); i++)
		{
			starsStr += "*";
		}
		System.out.println(starsStr);
		
		for(int i = 0; i < 8; i++)
		{
			for(int j = 0; j < 4; j ++)
			{
				if(this.exams[i][j].getGrade() != -1)
				{
					this.exams[i][j].print();
					System.out.print(" | ");
				}
			}
			System.out.println();
			System.out.println("--------------------");
			int fullMean = (int) Math.rint(calculateMean(i + 1, true));
			int relativeMean = (int) Math.rint(calculateMean(i + 1, false));
			System.out.printf("%s full mean: %s , relative mean: %s%n", this.exams[i][0].getCourseName(),fullMean , relativeMean);
			System.out.println("--------------------");
		}
	}
}
