import java.util.*;

public class Main {

	public static void main(String[] args) 
	{
		ArrayList<File> fileList = new ArrayList<File>(); //Create File List
		File a = new File("A", 100); // Create File 1
		File b = new File("B", 200); // Create File 2
		ImageFile c = new ImageFile("C", 300, 300, 100); // Create Image File 1
		ImageFile d = new ImageFile("D", 400, 200, 200); // Create Image File 2
		VideoFile e = new VideoFile("E", 500, true);	// Create Video File 1
		VideoFile f = new VideoFile("F", 600, false);	// Create Video File 2
		
		// Adding the file to Array List
		fileList.add(a);
		fileList.add(b);
		fileList.add(c);
		fileList.add(d);
		fileList.add(e);
		fileList.add(f);
		for(File file : fileList) // Print file details
		{
			System.out.println(file);
		}

	}

}
