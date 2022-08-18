package ex12;

import java.util.ArrayList;

public class PlayList {

	private ArrayList<Song> songs;
	
	public PlayList() {
	
		songs = new ArrayList<Song>();
	}
	
	/**
	 * adds a song at the end of the playlist
	 * @param s
	 */
	public void addSong(Song s)
	{
		songs.add(s);
	}
	
	/**
	 * plays a specific song from the playlist
	 * @param songName - the song name
	 * @param startAt - from which point to start playing the song
	 */
	public void playSong(String songName, int startAt)
	{
		Song s = find(songName);
		s.play(startAt);
	}

	/**
	 * plays a specific song from the playlist
	 * @param songNumber - the number of song in the list (should be 1 and greater)
	 * @param startAt - from which point to start playing the song
	 */
	public void playSong(int songNumber, int startAt) throws Exception
	{
		if(songNumber > songs.size())
		{
			throw new Exception("The num of song is higher then song list size");
		}
		else
		{
			Song s = songs.get(songNumber - 1);
			s.play(startAt);
		}
	}

	/**
	 * plays all songs currently on the playlist
	 */
	public void play()
	{
		for (Song song : songs) {
			song.play();
		}
	}

	/**
	 * finds a song insides the songs list
	 * @param songName 
	 * @return the song if found. otherwise returns null
	 */
	private Song find(String songName)
	{		
		for (Song song : songs) {
			if(song.getName().equals(songName))
				return song;
		}
		return null;
	}
}
