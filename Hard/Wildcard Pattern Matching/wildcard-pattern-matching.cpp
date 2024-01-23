//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;

// } Driver Code Ends

class Solution{
  public:
/*You are required to complete this method*/
    // 1 -> Memoization
    // int solve(int i, int j, string p, string str, vector<vector<int>> &dp) {
    //     if(i < 0 and j < 0) return 1;
    //     if(i < 0 and j >= 0) return 0;
    //     if(j < 0 and i >= 0) {
    //         for(int k = i; k >= 0; k--) 
    //             if(p[k] != '*')
    //                 return false;
    //         return true;
    //     }
    //     if(dp[i][j] != -1) return dp[i][j];
        
    //     if(p[i] == str[j] or p[i] == '?')
    //         return dp[i][j] = solve(i - 1, j - 1, p, str, dp);
    //     if(p[i] == '*')
    //         return dp[i][j] = solve(i - 1, j, p, str, dp) or solve(i, j - 1, p, str, dp);
    //     return dp[i][j] = 0;
    // }
    
    // int wildCard(string pattern,string str)
    // {
    //     int n = pattern.size(), m = str.size();
    //     vector<vector<int>> dp(n, vector<int> (m, -1));
    //     return solve(n - 1, m - 1, pattern, str, dp);
    // }
    
    // 2 -> Tabulation
    bool allStars(string &p, int i) {
        for(int k = 0; k < i; k++)
            if(p[k] != '*') return 0;
        return 1;
    }
    
    // int wildCard(string p, string str) {
    //     int n = p.size(), m = str.size();
    //     vector<vector<bool>> dp(n + 1, vector<bool>(m + 1, false));

    //     dp[0][0] = true;
        
    //       // i -> pattern (n) and j -> s (m)
    //     for (int j = 1; j <= m; j++)
    //         dp[0][j] = false; // i < 0 and j >= 0
        
    //     for (int i = 1; i <= n; i++)
    //         dp[i][0] = allStars(p, i); // j < 0 and i >= 0
        
    //     for (int i = 1; i <= n; i++) {
    //         for (int j = 1; j <= m; j++) {
    //           if (p[i - 1] == str[j - 1] or p[i - 1] == '?')
    //             dp[i][j] = dp[i - 1][j - 1];
    //           else if (p[i - 1] == '*')
    //             dp[i][j] = dp[i - 1][j] or dp[i][j - 1];
    //           else
    //             dp[i][j] = false;
    //         }
    //     }
        
    //     return dp[n][m];
    // }
    
    // 3 -> Space Optimization
    int wildCard(string p, string str) {
        int n = p.size(), m = str.size();
        vector<int> prev(m + 1, 0), curr(m + 1, 0);
        prev[0] = 1;
        
        for(int i = 1; i <= n; i++) {
            curr[0] = allStars(p, i); // j becomes 0
            for(int j = 1; j <= m; j++) {
                if(p[i - 1] == str[j - 1] or p[i - 1] == '?')
                    curr[j] = prev[j - 1];
                else if(p[i - 1] == '*')
                    curr[j] = prev[j] or curr[j - 1];
                else 
                    curr[j] = 0;
            }
            prev = curr;
        }
        
        return prev[m];
    }
    
};

//{ Driver Code Starts.
int main()
{
   int t;
   cin>>t;
   while(t--)
   {
           string pat,text;
           cin>>pat;
cin.ignore(numeric_limits<streamsize>::max(),'\n');
           cin>>text;
           Solution obj;
           cout<<obj.wildCard(pat,text)<<endl;
   }
}

// } Driver Code Ends