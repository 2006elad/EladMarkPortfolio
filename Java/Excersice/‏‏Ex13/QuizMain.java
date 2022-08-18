public class QuizMain {

	public static void main(String[] args) throws InterruptedException //Why do we need to throw exception here?
	{
		//#1 - first run
//		Quiz q = new Quiz();
//		q.run();//present quiz question
		

		//#2 - second run
		Quiz q = new Quiz();
		q.start();

		
	    int seconds = 0;
	    int minutes = 0;
	    
	    //#4 present timer
	    System.out.println("Timer:");
	    while(!q.getStatus())//
	    {
	    	Thread.sleep(1000);//#3 - which thread is this?
	    	seconds++;
	        if(seconds == 60)
	        {
	            seconds = 0;
	            minutes++;      
	        }	
	        System.out.println(minutes + ":" + seconds);
	    }
	    System.out.println("end of main");
		
	}
}
