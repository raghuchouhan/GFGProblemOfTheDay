//{ Driver Code Starts
// Initial Template for Java

import java.io.*;
import java.util.*;
class GFG {
    public static void main(String args[]) throws IOException {
        BufferedReader read =
            new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(read.readLine());
        while (t-- > 0) {
            int N, M, x, y;
            String S[] = read.readLine().split(" ");
            N = Integer.parseInt(S[0]);
            M = Integer.parseInt(S[1]);
            int a[][] = new int[N][M];
            for (int i = 0; i < N; i++) {
                String s[] = read.readLine().split(" ");
                for (int j = 0; j < M; j++) a[i][j] = Integer.parseInt(s[j]);
            }
            String s1[] = read.readLine().split(" ");
            x = Integer.parseInt(s1[0]);
            y = Integer.parseInt(s1[1]);
            Solution ob = new Solution();
            System.out.println(ob.shortestDistance(N, M, a, x, y));
        }
    }
}
// } Driver Code Ends


// User function Template for Java

class Pair{
    int a;//a equal to x-axis
    int b;//b equal to y-axis
    int step;
    Pair(int a,int b,int step){
        this.a = a;
        this.b = b;
        this.step = step;
    }
}

class Solution {
    int shortestDistance(int n, int m, int arr[][], int X, int Y) {
       
       if(arr[0][0] == 0 || arr[X][Y] == 0){
           return -1;
       }
       
       int dx[] = {0,0,-1,1};
       int dy[] = {-1,1,0,0};
       Queue<Pair> q = new LinkedList<>();
       int ans = Integer.MAX_VALUE;
       boolean visited[][] = new boolean[n][m];
       q.add(new Pair(0,0,0));
       visited[0][0] = true;
       
       //start BFS
       while(!q.isEmpty()){
           Pair val = q.poll();
           if(val.a == X && val.b == Y){
               ans = Integer.min(ans,val.step);
           }else{
               for(int i=0;i<4;i++){//according to the question we only traverse 4 direction .
                   if(check(arr,val,i,dx,dy,visited)){
                       q.add(new Pair(val.a+dx[i],val.b+dy[i],val.step+1));
                       visited[val.a+dx[i]][val.b+dy[i]] = true;
                   }
               }
           }
       }
       return (ans==Integer.MAX_VALUE)?-1:ans;
    }
    public static boolean check(int arr[][],Pair val,int i,int dx[],int dy[],boolean visited[][]){
        
        
        if(val.a+dx[i]<0 || val.b+dy[i]<0 || val.a+dx[i]>=arr.length 
            || val.b+dy[i]>=arr[0].length || arr[val.a+dx[i]][val.b+dy[i]] == 0 
                        || visited[val.a+dx[i]][val.b+dy[i]] == true ){
                        return false;
                    }
        
        return true;
    }
};