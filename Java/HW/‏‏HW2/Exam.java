/**
 * Class that represent an one exam with course code(1-8), num of quarter(between 1-4) and the grade
 *
 */
public class Exam 
{
	private int course;
	private int quarter;
	private int grade;
	public Exam(int course, int quarter, int grade) 
	{
		this.course = course;
		this.quarter = quarter;
		this.grade = grade;
	}
	public Exam(Exam other) 
	{
		this.course = other.course;
		this.quarter = other.quarter;
		this.grade = other.grade;
	}
	public int getCourse() {
		return course;
	}
	public int getQuarter() {
		return quarter;
	}
	public int getGrade() {
		return grade;
	}
	public void setGrade(int grade) {
		this.grade = grade;
	}
	/**
	 * Function that return the name of the course
	 * @return String: name of the course
	 */
	public String getCourseName()
	{
		switch(this.course)
		{
			case 1:
				return "Math";
			case 2:
				return "English";
			case 3:
				return "Bible";
			case 4:
				return "History";
			case 5:
				return "Literature";
			case 6:
				return "Gym";
			case 7:
				return "Science";
			default:
				return "Citizenship";
		}
	}
	/**
	 * Function that print a full message that include: course name, the quarter and the grade
	 */
	public void print()
	{
		System.out.printf("%s(%s): %s", this.getCourseName(), this.quarter,this.grade);

	}	
}
