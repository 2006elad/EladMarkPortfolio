package ex5;

public class App 
{
	private String name;
	private int size;
	private boolean isRunning;
	public App(String name, int size) {
		this.name = name;
		this.size = size;
		this.isRunning = false;
	}
	public App(App other) {
		this.name = other.name;
		this.size = other.size;
		this.isRunning = other.isRunning;
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public int getSize() {
		return size;
	}
	public void setSize(int size) {
		this.size = size;
	}
	public boolean isRunning() {
		return isRunning;
	}
	public void setRunning(boolean isRunning) {
		this.isRunning = isRunning;
	}
	
}
