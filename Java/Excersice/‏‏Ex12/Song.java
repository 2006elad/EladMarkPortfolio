package ex12;

public class Song {

	private String name;
	private int seconds;

	public Song(String name, int seconds) throws Exception{
		this.name = name;
		if(seconds < 0)
		{
			throw new Exception("Song duration must be greater than 0");
		}
		else
		{
			this.seconds = seconds;
		}
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public int getSeconds() {
		return seconds;
	}

	public void setSeconds(int seconds) {
		this.seconds = seconds;
	}

	/**
	 * this method shows the name of the song and its full play time
	 */
	public void play()
	{
		play(0);
	}
	
	/**
	 * this method shows the name of the song and partial play time  
	 * @param startAt - a non negative number not greater than song's seconds
	 */
	public void play(int startAt)
	{
		System.out.printf("Playing %s. Play time is %d.\n", name, seconds - startAt);
	}
}
