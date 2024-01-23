//{ Driver Code Starts
// Initial Template for Java

import java.util.*;
class Rat {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();

        while (t-- > 0) {
            int n = sc.nextInt();
            int[][] a = new int[n][n];
            for (int i = 0; i < n; i++)
                for (int j = 0; j < n; j++) a[i][j] = sc.nextInt();

            Solution obj = new Solution();
            ArrayList<String> res = obj.findPath(a, n);
            Collections.sort(res);
            if (res.size() > 0) {
                for (int i = 0; i < res.size(); i++)
                    System.out.print(res.get(i) + " ");
                System.out.println();
            } else {
                System.out.println(-1);
            }
        }
    }
}

// } Driver Code Ends


// User function Template for Java

// m is the given matrix and n is the order of matrix
class Solution {
  static ArrayList<String>ans=new ArrayList<>();
    public static ArrayList<String> findPath(int[][] m, int n) {
        // Your code here
        ans.clear();
        // boolean[][] vis=new boolean[n][n];
      
            helper(m,n,0,0,"");
    
        return ans;
    }
    
    public static void helper(int[][]arr,int n,int row,int col,String path)
    {
       
        if(row<0 || row>=n || col<0 || col>=n || arr[row][col]==0 )
        return ;
        
         if(row==n-1 && col==n-1 )
        {
           
            ans.add(path);
            return ;
        }
        
        //no need to use extra space to keep track of the visted elements so i ave modified the original array itself
            arr[row][col]=0;
            helper(arr,n,row+1,col,path+"D");
            helper(arr,n,row,col+1,path+"R");
            helper(arr,n,row-1,col,path+"U");
            helper(arr,n,row,col-1,path+"L");
            arr[row][col]=1;
             
        
    }
    
}