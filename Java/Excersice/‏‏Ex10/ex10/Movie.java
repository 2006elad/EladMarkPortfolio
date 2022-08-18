package ex10;
public class Movie 
{
	private String title;
	private int minutes;
	private int genre;
	private final static String[] MOVIE_GENRES = {"Thriller", "Comedy", "Drama", "ScienceFiction", "Documentary", "Other"};
	private static int otherMinutes = 0; 
	
	public Movie(String title, int minutes, int genre) {
		this.title = title;
		this.minutes = minutes;
		if(!(genre <=1 && genre <=5))
		{
			this.genre = 6;
			otherMinutes += this.minutes;
		}
		else
		{
			this.genre = genre;	
		}
	}
	public String getTitle() {
		return title;
	}
	public void setTitle(String title) {
		this.title = title;
	}
	public int getMinutes() {
		return minutes;
	}
	public void setMinutes(int minutes) 
	{
		if(this.genre == 6)
		{
			if(minutes < 0)
			{
				this.minutes -= this.minutes;
				otherMinutes += 0;
			}
			else
			{
				this.minutes -= this.minutes;
				otherMinutes += minutes;
			}
		}
		else
		{
			if(minutes < 0)
			{
				this.minutes -= this.minutes;
			}
			else
			{
				this.minutes -= this.minutes;
			}
		}
	}
	public int getGenre() {
		return genre;
	}
	public void setGenre(int genre) 
	{
		if(!(genre <=1 && genre <=5))
		{
			if(this.genre != 6)
			{
				this.genre = 6;
				otherMinutes += this.minutes;
			}
		}
		else
		{
			if(this.genre == 6)
			{
				otherMinutes -= this.minutes;
				this.genre = genre;
			}
		}
	}
	public static String getGenreName(int g)
	{
		
		if(!(g <=1 && g <=5))
		{
			return MOVIE_GENRES[g-1];
		}
		else
		{
			return MOVIE_GENRES[5];
		}
	}
	
	public static int getOtherMinutes() {
		return otherMinutes;
	}
	public static void setOtherMinutes(int otherMinutes) {
		Movie.otherMinutes = otherMinutes;
	}
	@Override
	public String toString() 
	{
		return String.format("The Name of the movie is: %s, The duration of the movie is: %s, The Genre of the movie is: %s" , this.title, this.minutes, MOVIE_GENRES[this.genre -1]);
	}
	
}
