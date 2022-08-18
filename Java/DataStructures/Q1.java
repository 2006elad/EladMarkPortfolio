//	Lior Hazoom - 205972078 
//	Elad Mark - 316293638

public class Q1 
{
	static Node buildBST(int arr[], int n)
	{
		Node root = new Node(arr[0]);
		for(int i=1;i<n;i++)
		{
			root.insertRecursive(root, arr[i]);
		}
		return root;
	}
}
