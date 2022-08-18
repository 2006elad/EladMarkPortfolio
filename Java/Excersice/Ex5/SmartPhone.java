package ex5;

import java.util.ArrayList;

public class SmartPhone 
{
	private int memory;
	private ArrayList<App> apps;
	public SmartPhone(int memory) {
		this.memory = memory;
		this.apps = new ArrayList<App>();
	}
	public int getMemory() {
		return memory;
	}
	public ArrayList<App> getApps() {
		return apps;
	}
	public void install(App appCopy)
	{
		if(appCopy.getSize()<this.memory && isExsist(appCopy.getName()) != -1)
		{
			this.memory -= appCopy.getSize();
			this.apps.add(appCopy);
			System.out.println("App installed memory updated");
		}
		else
		{
			System.out.println("App didn't installed");
		}
	}
	private int isExsist(String name)
	{
		int index = 0;
		while(index<this.apps.size())
		{
			if(this.apps.get(index).getName().equals(name))
			{
				return index;
			}
		}
		return -1;
	}
	public void startApp(String appName)
	{
		if(isExsist(appName) != -1)
		{
			int index = isExsist(appName);
			if(this.apps.get(index).isRunning() != true)
			{
				this.apps.get(index).setRunning(true);	
			}
			else
			{
				System.out.println("App already Running");
			}
		}
		else
		{
			System.out.println("App didn't exsist");
		}
	}
	public void stopApp(String appName)
	{
		if(isExsist(appName) != -1)
		{
			int index = isExsist(appName);
			if(this.apps.get(index).isRunning() != false)
			{
				this.apps.get(index).setRunning(false);	
			}
			else
			{
				System.out.println("App already not Running");
			}
		}
		else
		{
			System.out.println("App didn't exsist");
		}
	}
	public void shutDown()
	{
		for(int i = 0; i<this.apps.size();i++)
		{
			this.apps.get(i).setRunning(false);
		}
	}
	public void uninstall(String name)
	{
		int index = isExsist(name);
		if(index != -1)
		{
			this.memory += this.apps.get(index).getSize();
			this.apps.remove(index);
		}
		else
		{
			System.out.println("App didn't exsist");
		}
	}
	public void print(int choice)
	{
		switch (choice)
		{
			case 1:
				for(App currentApp:apps)
				{
					readyMessage(currentApp);
				}
			case 2:
				for(App currentApp:apps)
				{
					if(currentApp.isRunning() == true)
					{
						readyMessage(currentApp);
					}
				}
			case 3:
				for(App currentApp:apps)
				{
					if(currentApp.isRunning() == false)
					{
						readyMessage(currentApp);
					}
				}
		}
	}
	private void readyMessage(App currentApp)
	{
		System.out.printf("App Name: %s/tSize: %s\tis App Running: %s\n",currentApp.getName(),currentApp.getSize(),currentApp.isRunning());
	}
}
