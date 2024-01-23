//{ Driver Code Starts
// Initial Template for Java
import java.util.*;
import java.lang.*;
import java.io.*;
class GFG
{
    public static void main(String[] args) throws IOException
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine().trim());
        while(T-->0)
        {
            String[] s = br.readLine().trim().split(" ");
            int V = Integer.parseInt(s[0]);
            int E = Integer.parseInt(s[1]);
            ArrayList<ArrayList<Integer>>adj = new ArrayList<>();
            for(int i = 0; i < V; i++)
                adj.add(i, new ArrayList<Integer>());
            for(int i = 0; i < E; i++){
                String[] S = br.readLine().trim().split(" ");
                int u = Integer.parseInt(S[0]);
                int v = Integer.parseInt(S[1]);
                adj.get(u).add(v);
                adj.get(v).add(u);
            }
            Solution obj = new Solution();
            ArrayList<Integer>ans = obj.articulationPoints(V, adj);
            for (int i =0 ;i < ans.size (); i++) 
                System.out.print (ans.get (i) + " ");
            System.out.println();
        }
    }
}

// } Driver Code Ends

class Solution
{   public static int time = 0;
    //Function to return Breadth First Traversal of given graph.
    public ArrayList<Integer> articulationPoints(int V,ArrayList<ArrayList<Integer>> adj)
    {
        // Code here
        int[] tim = new int[V];
        int [] low = new int[V];
        int mark[] = new int[V];
        for(int i = 0 ; i < V ; i ++)
        {
            if(tim[i]==0)
            dfs(adj,i,-1,tim,low,mark);
        }
        ArrayList<Integer> ans = new ArrayList<>();
        for(int i = 0 ; i < V ; i ++)if(mark[i]==1)ans.add(i);
        if(ans.size()==0) ans.add(-1);
        return ans;
        
    }
    public void dfs(ArrayList<ArrayList<Integer>> adj,int curr , int par , int[]tim , int[]low,int[]mark)
    {
        time++;
        tim[curr]=low[curr]=time;
        int child=0;
        for(int neigh : adj.get(curr))
        {
            if(neigh==par)continue;
            if(tim[neigh]==0)
            {
                dfs(adj,neigh,curr,tim,low,mark);
                low[curr]=Math.min(low[curr],low[neigh]);
                if(low[neigh]>=tim[curr] && par!=-1)mark[curr]=1;
                child++;
            }
            else{
                low[curr]=Math.min(low[curr],tim[neigh]);
            }
            
        }
        if(par==-1 && child>1)
        {   
            mark[curr]=1;
        }
    }
}
