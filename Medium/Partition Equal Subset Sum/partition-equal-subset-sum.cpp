//{ Driver Code Starts
// Initial Template for C++

#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
// User function Template for C++

class Solution{
private:
    bool solve(int arr[], int N, int index, int target, vector<vector<int>>&dp){
        // base cases
        if(index >= N) return 0;
        if(target < 0) return 0;
        if(target == 0) return 1;
        
        if(dp[index][target] != -1) return dp[index][target];
        
        bool include = solve(arr, N, index+1, target-arr[index], dp);
        bool exclude = solve(arr, N, index+1, target, dp);
        
        dp[index][target] = include || exclude;
        return dp[index][target];
    }
public:
    int equalPartition(int N, int arr[]){
        int total = 0;
        for(int i=0; i<N; i++) total += arr[i];
        if(total&1) return 0;
        int target = total/2;
        vector<vector<int>>dp(N+1, vector<int>(target+1, -1));
        return solve(arr, N, 0, target, dp);
    }
};

//{ Driver Code Starts.

int main(){
    int t;
    cin>>t;
    while(t--){
        int N;
        cin>>N;
        int arr[N];
        for(int i = 0;i < N;i++)
            cin>>arr[i];
        
        Solution ob;
        if(ob.equalPartition(N, arr))
            cout<<"YES\n";
        else
            cout<<"NO\n";
    }
    return 0;
}
// } Driver Code Ends