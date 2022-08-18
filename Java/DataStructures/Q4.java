//	Lior Hazoom - 205972078 
//	Elad Mark - 316293638

public class Q4 
{
	static int closest_num(Node node, int num)
	{
		Node curRoot = node;
		int temp = curRoot.key;
		while(curRoot != null)
		{
			if((Math.abs(curRoot.key - num)) < Math.abs(temp - num))
			{
				temp = curRoot.key;
			}
			if(num<curRoot.key)
			{
				curRoot = curRoot.left;
			}
			else
			{
				curRoot = curRoot.right;
			}
		}
		return temp;
	}
}