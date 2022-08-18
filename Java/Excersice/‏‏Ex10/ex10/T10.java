package ex10;

public class T10 {

	public static void main(String[] args) 
	{
		Movie a = new Movie("Monkeys Twelve", 120, 4);
		System.out.println(Movie.getOtherMinutes());
		Movie b = new Movie("Misery ", 110, 6);
		b.setMinutes(120);
		System.out.println(Movie.getOtherMinutes());
		b.setGenre(1);
		System.out.println(Movie.getOtherMinutes());
		System.out.println(a);
		System.out.println(Movie.getGenreName(a.getGenre() -1));
		

	}

}
