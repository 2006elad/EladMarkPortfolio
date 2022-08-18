//	Lior Hazoom - 205972078 
//	Elad Mark - 316293638

import java.util.*;
public class Main
{	
	// Function that print the tree in order to check if the tree is ordered correct
	static void inorder_Recursive(Node root) 
	{ 
	        if (root != null) 
	      { 
	            inorder_Recursive(root.left); 
	            System.out.print(root.key + " "); 
	            inorder_Recursive(root.right); 
	      } 
	 }
	public static void main(String[] args) 
	{
		//Q1 EXAMPLE CHECK		
//		int[] arr = {4,2,3,7,2,6,1}; 
//		Node root = Q1.buildBST(arr,7); 
		
		//Q2 EXAMPLE CHECK
//		int[] arr = {20, 6, 5,15,3,6};
//		Node root = Q1.buildBST(arr,6); 
//		Q2.printNodesWithEvenLeaves(root)
		
		//Q3 EXAMPLE CHECK
//		int[] arr = {2, 5, 9, 1, 6, 8, 4}; 
//		Node root = Q1.buildBST(arr,6); 
//		ArrayList<Integer> arr = new ArrayList<Integer>();
//		Q3.printAllpaths(root, arr);
		
		//Q4 EXAMPLE CHECK
//		int[] arr = {12, 7, 15, 5, 8, 13, 22, 2, 6, 11, 14}; 
//		Node root = Q1.buildBST(arr,11); 
//		Q4.closest_num(root, 9)


//		inorder_Recursive(root);
//		System.out.println(closest_num(root, 9));
	}
}
