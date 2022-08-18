package ex5;

public class Main {

	public static void main(String[] args) 
	{
		SmartPhone s1 = new SmartPhone(1000);
		SmartPhone s2 = new SmartPhone(250);
		App waze = new App("Waze", 80);
		App whatsapp = new App("Whatsapp", 125);
		App pango = new App("Pango", 60);
		s1.install(waze);
		s1.install(pango);
		s1.install(whatsapp);
		s2.install(waze);
		s2.install(pango);
		s2.install(whatsapp);
		s1.startApp(waze.getName());
		s1.startApp(pango.getName());
		s2.s
		
	}

}
