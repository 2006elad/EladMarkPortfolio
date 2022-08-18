//	Lior Hazoom - 205972078 
//	Elad Mark - 316293638

public class Node 
{
	public int key;
	public Node left;
	public Node right;
	public Node(int key) 
	{
		this.key = key;	
	}
	
	Node insertRecursive(Node root, int key) 
	{ 
      if (root == null) { 
          root = new Node(key); 
          return root; 
      } 
      if (key <= root.key)
      {
          root.left = insertRecursive(root.left, key); 
      }
      else if (key > root.key)
      {
          root.right = insertRecursive(root.right, key); 
      }
      return root; 
  } 
}
