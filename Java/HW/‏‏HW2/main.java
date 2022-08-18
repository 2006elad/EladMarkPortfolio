import java.util.Scanner;


public class main 
{
	/**
	 * 	Function that return the name of a specific course the function is for printing purposes when user input for each test the grade(this function is the same as method in exam class, but because we print the name without using exam class then we need extra function to print the name)
	 * @param courseNum - the code of the course we want to find his name
	 * @return - String: name of the course
	 */
	public static String getCourseName(int courseNum)
	{
		switch(courseNum)
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
				return "Sports";
			case 7:
				return "Science";
			default:
				return "Citizenship";
		}
	}

	public static void main(String[] args) 
	{
		Scanner input = new Scanner(System.in);
		GradeSheet[] students = new GradeSheet[1];
		for(int i = 0; i < students.length; i++)
		{
			String studentName;
			System.out.println("Please insert student Number " + (i+1) + " Name:");
			studentName = input.nextLine();
			students[i] = new GradeSheet(studentName);
			for(int j = 0; j< 8; j++)
			{
				System.out.println("****" + getCourseName(j + 1) + " Grades****");
				for(int k = 0; k < 4; k++)
				{
					System.out.printf("Please insert the test grade(0-100) of quarter number: %d%nPlease insert -1 if you didn't do the test:", (k+1));
					int grade = input.nextInt();
					Exam currentTest = new Exam((j+1),(k+1), grade);
					students[i].addOneExam(currentTest);
				}
				System.out.println();
			}
		}
		students[0].Print();
		input.close();
	}
}
