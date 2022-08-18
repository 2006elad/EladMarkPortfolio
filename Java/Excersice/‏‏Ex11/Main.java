package ex11;
import java.util.*;

public class Main {

	public static void main(String[] args)
	{
		Rectangle rec = new Rectangle(3, '*', 5);
		Triangle tri = new Triangle(5, '#', true);
		Photo photo = new Photo(13, 40,"   (%%%%%%%%.              %%%%%%%%%      %%#.....,%%/           .%%(.....(%%     %##.....,%%#%%%#####%%%#%%/.....(%%      #%%%%%%%%###############%#%%%%%%%           ,%######################(              /%####%%%%#######%%%%####%#             %###%*%@@ %%####%.@@@ %###%*           /%####%.. ##%%##%%#.. #%###%#           .%######%%#**@@@/*(%########/            (%#####%*(*******(*#%####%#              *%%###%*@**#%%**&*%%##%%#                 /%%##%%(((#(((%%##%%#                      ,##########%#%/             ");
		ArrayList<Drawable> drawableList = new ArrayList<Drawable>();
		drawableList.add(rec);
		drawableList.add(tri);
		drawableList.add(photo);
//		for(Drawable draw:drawableList)
//		{
//			draw.draw();
//			System.out.println("\n\n\n");
//		}
		ArrayList<Enlargeable> enLargeList = new ArrayList<Enlargeable>();
		enLargeList.add(rec);
		enLargeList.add(photo);
//		for(Enlargeable enlarge:enLargeList)
//		{
//			enlarge.enlarge(4);
//		}
		for(Drawable draw:drawableList)
		{
//			draw.draw();
//			System.out.println("\n\n\n");
			draw.abc();
		}
//		photo.draw();
	}

}
