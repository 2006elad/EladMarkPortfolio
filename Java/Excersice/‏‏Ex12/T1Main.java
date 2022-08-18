package ex12;

public class T1Main {

	public static void main(String[] args) 
	{
		PlayList pl = new PlayList();
		pl.addSong(new Song("S1", 180));
		pl.addSong(new Song("S2", 200));
		
		//play first song from the beginning
		pl.playSong(1, 0);
		//play second song from its midst 
		pl.playSong("S2", 100);
		
		//WHAT IS THE PROBLEM WITH THE FOLLOWING INSTRUCTIONS?
		//Song s3 = new Song("S3", -240);
		//pl.playSong(1, 190);		
		//pl.playSong("S3", 0);		
		//pl.playSong(5, 100);		
	}
}
