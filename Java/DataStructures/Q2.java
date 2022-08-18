//	Lior Hazoom - 205972078 
//	Elad Mark - 316293638

public class Q2 
{
	static int printNodesWithEvenLeaves(Node root)
	{
		if(root == null)
		{
			return 0;
		}
		
		if(root.left == null && root.right == null)
		{
			return 1;
		}
		
		int sumOfleavesLeft = printNodesWithEvenLeaves(root.left);
		int sumOfleavesRight = printNodesWithEvenLeaves(root.right);
		
		if((sumOfleavesLeft % 2) == 0 || (sumOfleavesRight%2) == 0)
		{
			System.out.println(root.key);
		}
		
		return sumOfleavesLeft + sumOfleavesRight;
	}

}
