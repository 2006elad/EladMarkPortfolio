//	Lior Hazoom - 205972078 
//	Elad Mark - 316293638


import java.util.ArrayList;

public class Q3 
{
	static void printAllpaths(Node root, ArrayList<Integer> list)
	{
		if(root != null)
		{
			list.add(root.key);
			if(root.left == null && root.right == null)
			{
				for(int key:list)
				{
					System.out.print(key + " ");
				}
				System.out.println();
				list.remove(list.size() - 1);
			}
			else
			{
				printAllpaths(root.left, list);
				printAllpaths(root.right, list);
				list.remove(list.size() -1);
			}
		}
	}
}
