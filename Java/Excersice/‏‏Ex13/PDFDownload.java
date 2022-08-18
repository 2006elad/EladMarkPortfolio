import java.io.*;
import java.net.*;

public class PDFDownload implements Runnable
{
	private static int count = 1;

	private String urlAddress;
	private long fileSize;
	private String localFilePath;
	private int downloaded;
	private int fileId;
	
	public PDFDownload(String urlAddress) 
	{
		this.urlAddress = urlAddress;
		this.fileId = count;
		this.localFilePath = System.getProperty("user.home") + "\\Downloads\\" + fileId + ".pdf";
		count++;
	}

	public long getFileSize() { return fileSize;}
	
	public int getDownloaded() {return downloaded;}
	
	public int getFileId() {return fileId;}
	
	public void run()
	{
		setFileSize();
		download();		
	}
	
	/**
	 * this method actually downloads a file
	 * from the Internet chunk by chunk
	 * code credits to https://stackoverflow.com/questions/921262/how-can-i-download-and-save-a-file-from-the-internet-using-java
	 */
    private void download() 
    {
        OutputStream out = null;
        URLConnection conn = null;
        InputStream in = null;

        try 
        {
            URL url = new URL(urlAddress);
            out = new BufferedOutputStream(new FileOutputStream(localFilePath));
            conn = url.openConnection();
            in = conn.getInputStream();
            byte[] buffer = new byte[1024];

            int numRead;
            long numWritten = 0;

            while ((numRead = in.read(buffer)) != -1) 
            {
                out.write(buffer, 0, numRead);
                numWritten += numRead;
                //sleep(10);
                downloaded = (int)(100 * numWritten / fileSize);
            }
        } 
        catch (Exception e) 
        { 
            e.printStackTrace();
        } 
        finally 
        {
            try 
            {
                if (in != null) 
                {
                    in.close();
                }
                if (out != null) 
                {
                    out.close();
                }
            } 
            catch (IOException ioe) {
            }
        }
    }

    /**
     * this method simulates finding the file's size
     * in order to be able to calculate download percent
     */
    private void setFileSize()
    {
        URLConnection conn = null;
        InputStream in = null;

        try {
            URL url = new URL(urlAddress);
            conn = url.openConnection();
            in = conn.getInputStream();
            byte[] buffer = new byte[1024];

            int numRead;
            long numWritten = 0;

            while ((numRead = in.read(buffer)) != -1) {
                numWritten += numRead;
            }
            fileSize= numWritten;
        } 
        catch (Exception e) { 
            e.printStackTrace();
        } 
        finally {
            try {
                if (in != null) {
                    in.close();
                }
            } 
            catch (IOException ioe) {
            }
        }        
    }
}
