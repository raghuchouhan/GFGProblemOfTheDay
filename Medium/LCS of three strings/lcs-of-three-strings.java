//{ Driver Code Starts
//Initial Template for Java
import java.io.*;
import java.util.*; 
class GFG{
    public static void main(String args[]) throws IOException 
    { 
        BufferedReader read = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(read.readLine());
        while(t-- > 0){
            String input_line[] = read.readLine().trim().split("\\s+");
            int n1 = Integer.parseInt(input_line[0]);
            int n2 = Integer.parseInt(input_line[1]);
            int n3 = Integer.parseInt(input_line[2]);
            input_line = read.readLine().trim().split("\\s+");
            String A = input_line[0];
            String B = input_line[1];
            String C = input_line[2];
            Solution obj = new Solution();
            System.out.println(obj.LCSof3(A, B, C, n1, n2, n3));
        }
    } 
} 
// } Driver Code Ends

//User function Template for Java
class Solution 
{ 
    int LCSof3(String A, String B, String C, int n1, int n2, int n3) 
    { 
        // code here
        int[][][] dp = new int[n1+1][n2+1][n3+1];
        for (int i = 0; i <= n1; i++) {
        for (int j = 0; j <= n2; j++) {
        for (int k = 0; k <= n3; k++) {
            dp[i][j][k] = -1;
        }
    }
}
      return Helper(A,B,C,n1,n2,n3,0,0,0,dp);
       
       
        
    }
    int Helper(String A,String B,String C,int n1,int n2,int n3,int i,int j,int k,int[][][]dp){
        
        if(i > n1-1 || j > n2-1 || k > n3-1) return 0;
        
        if(dp[i][j][k] != -1) return dp[i][j][k];
        
        if(A.charAt(i) == B.charAt(j) && B.charAt(j) == C.charAt(k)){
            dp[i][j][k] = 1 + Helper(A,B,C,n1,n2,n3,i+1,j+1,k+1,dp);
        }else{
            dp[i][j][k] = Math.max(Helper(A,B,C,n1,n2,n3,i+1,j,k,dp),
            Math.max(Helper(A,B,C,n1,n2,n3,i,j+1,k,dp),
            Helper(A,B,C,n1,n2,n3,i,j,k+1,dp)));
        }
        return dp[i][j][k];
    }
}
