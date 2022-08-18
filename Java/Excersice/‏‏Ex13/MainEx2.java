public class MainEx2 {

	public static void main(String[] args) 
	{   //PDF files links: https://www.infobooks.org/free-programming-books-pdf/
		Thread th1, th2, th3;
		PDFDownload fd1 = new PDFDownload("https://www-personal.acfr.usyd.edu.au/tbailey/ctext/ctext.pdf");
		th1 = new Thread(fd1);
		//PDFDownload fd2 = new PDFDownload("https://www.iitk.ac.in/esc101/share/downloads/javanotes5.pdf");
		PDFDownload fd2 = new PDFDownload("https://www.introprogramming.info/wp-content/uploads/2013/07/Books/CSharpEn/Fundamentals-of-Computer-Programming-with-CSharp-Nakov-eBook-v2013.pdf");
		th2 = new Thread(fd2);
		PDFDownload fd3 = new PDFDownload("https://www.introprogramming.info/wp-content/uploads/2013/07/Books/CSharpEn/Fundamentals-of-Computer-Programming-with-CSharp-Nakov-eBook-v2013.pdf");
		th3 = new Thread(fd3);
		
		
		Thread[] arr = {th1};
		PDFDownload[] arr2 = {fd1};
		//PDFDownload[] arr = {fd2, fd3};
		th2.setPriority(Thread.MAX_PRIORITY);
		for (Thread file : arr) 
		{
			//file.run();
			file.start();
		}
		//fd3.setPriority(Thread.MIN_PRIORITY);
		/*
		 *WHILE LOOP  STOPS WHEN ALL PDF FILES DOWNLOADING COMPLETED
		 */
		boolean downloading = true;
		int outputSize = 0;
		while(downloading)
		{
			int completed = 0;
			clearScreen(outputSize);
			outputSize = 0;
			for (PDFDownload item : arr2) 
			{
				outputSize += printProgress(item);				
				if(item.getDownloaded() == 100)
					completed++;
			}
			downloading = completed < arr.length;					
		}
		
		
		System.out.print("\nAll pdf files downloaded");
	}

	/**
	 * this function prints download progress of a single PDF file download
	 * @param item - the item which progress is being shown
	 * @return the amount of characters that are being written to the console
	 */
    public static int printProgress(PDFDownload item)
    {
    	String output = String.format("pdf %d: |", item.getFileId());
		int mid = item.getDownloaded() / 4;
		for (int j = mid; j > 0; j--) {				
			output += "#";
		}
		for(int j = mid; j < 25; j++)
			output += "_";
		output += String.format("| (%d%%) ", item.getDownloaded());
		System.out.print(output);
		return output.length();
    }

    /**
     * this function clears former text shown on the console
     * thus better simulating a dynamic view of a progress bar
     * @param amount - the size of the text printed on the console
     */
    public static void clearScreen(int amount)
    {
    	while(amount > 0)
    	{
    		System.out.print("\b");
    		amount--;
    	}
    }
}
