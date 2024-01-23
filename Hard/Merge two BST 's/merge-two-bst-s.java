//{ Driver Code Starts
//Initial Template for Java

/*package whatever //do not write package name here */

import java.io.*;
import java.util.*;
import java.math.*;

class Node  
{ 
    int data; 
    Node left, right; 
   
    public Node(int d)  
    { 
        data = d; 
        left = right = null; 
    } 
}

class GFG
{
    static Node buildTree(String str)
    {
        // Corner Case
        if(str.length() == 0 || str.equals('N'))
            return null;
        String[] s = str.split(" ");
        
        Node root = new Node(Integer.parseInt(s[0]));
        Queue <Node> q = new LinkedList<Node>();
        q.add(root);
        
        // Starting from the second element
        int i = 1;
        while(!q.isEmpty() && i < s.length)
        {
              // Get and remove the front of the queue
              Node currNode = q.remove();
        
              // Get the curr node's value from the string
              String currVal = s[i];
        
              // If the left child is not null
              if(!currVal.equals("N")) 
              {
        
                  // Create the left child for the curr node
                  currNode.left = new Node(Integer.parseInt(currVal));
        
                  // Push it to the queue
                  q.add(currNode.left);
              }
        
              // For the right child
              i++;
              if(i >= s.length)
                  break;
              currVal = s[i];
        
              // If the right child is not null
              if(!currVal.equals("N")) 
              {
        
                  // Create the right child for the curr node
                  currNode.right = new Node(Integer.parseInt(currVal));
        
                  // Push it to the queue
                  q.add(currNode.right);
              }
              
              i++;
        }
    
        return root;
    }
    
    public static void main(String args[]) throws IOException {
    
       BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine().trim());
        while(t>0)
        {
            String s = br.readLine();
            Node root1 = buildTree(s);
            
            s = br.readLine();
            Node root2 = buildTree(s);
            
            Solution T = new Solution();
            List<Integer> ans = T.merge(root1,root2);
            for(int i=0;i<ans.size();i++)
                System.out.print(ans.get(i) + " ");
            System.out.println();
            
            t--;
        }
    }
}

// } Driver Code Ends


//User function Template for Java

class Solution{
    //Function to return a list of integers denoting the node 
    //values of both the BST in a sorted order.
    void inorder(Node root1,Node root2,Queue<Integer> s1,Queue<Integer> s2){
        if(root1==null && root2==null){
            return ;
        }
        
        else if(root2==null){
            inorder(root1.left,root2,s1,s2);
            s1.add(root1.data);
            inorder(root1.right,root2,s1,s2);
        }
        
        else if(root1==null){
            inorder(root1,root2.left,s1,s2);
            s2.add(root2.data);
            inorder(root1,root2.right,s1,s2);
        }
        else{
            inorder(root1.left,root2.left,s1,s2);
            s1.add(root1.data);
            s2.add(root2.data);
            inorder(root1.right,root2.right,s1,s2);}
    }
    
    public List<Integer> merge(Node root1,Node root2){
        List<Integer> l=new ArrayList<>();
        Queue<Integer> q1=new ArrayDeque<>();
        Queue<Integer> q2=new ArrayDeque<>();
        inorder(root1,root2,q1,q2);
        
      //  System.out.print(q1+ " "+q2+" " );
        
        while(!q1.isEmpty() && !q2.isEmpty()){
            int a=q1.peek();
            int b=q2.peek();
            if(a>b){
                l.add(b);
                q2.remove();
            }
            else{
                l.add(a);
                q1.remove();
            }
        }
        
        while(!q1.isEmpty()){
            l.add(q1.poll());
        }
        while(!q2.isEmpty()){
            l.add(q2.poll());
        }
        
        return l;
    }
}
