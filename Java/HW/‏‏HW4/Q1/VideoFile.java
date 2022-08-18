
public class VideoFile extends File
{
	private boolean hasTranslation;

	public VideoFile(String name, int bytes, boolean hasTranslation) {
		super(name, bytes);
		this.hasTranslation = hasTranslation;
	}
	public VideoFile(VideoFile other)
	{
		super(other);
		this.hasTranslation = other.hasTranslation;
	}
	public boolean isHasTranslation() {
		return hasTranslation;
	}
	public void setHasTranslation(boolean hasTranslation) {
		this.hasTranslation = hasTranslation;
	}
	@Override
	public String toString() 
	{
		String string = String.format("The file name is: %s, the size of the file is: %s. %s", this.getName(), this.getBytes(), this.hasTranslation == true ? "The video file has translation." : "The video file doesn't have any translation.");
		return string;
	}
	
	@Override
	public boolean equals(Object other) {
		if(getClass() == other.getClass())
		{
			VideoFile videoFile = (VideoFile) other;
			if(super.equals(other) && (videoFile.hasTranslation == this.hasTranslation))
			{
				return true;
			}
			else
			{
				return false;
			}
		}
		else
		{
			return false;
		}
	}
	

}
