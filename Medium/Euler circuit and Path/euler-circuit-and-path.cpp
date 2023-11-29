//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;

// } Driver Code Ends
#include <vector>
#include <unordered_set>

class Solution {
public:
    void dfs(int node, std::vector<int>& in_degree, std::unordered_set<int>& visited, const std::vector<int> adj[]) {
        visited.insert(node);
        for (int neighbor : adj[node]) {
            in_degree[neighbor]++;
            if (visited.find(neighbor) == visited.end()) {
                dfs(neighbor, in_degree, visited, adj);
            }
        }
    }

    int isEulerCircuit(int V, vector<int> adj[]) {
        std::vector<int> in_degree(V, 0);
        std::unordered_set<int> visited;

        // Perform DFS and calculate in-degrees
        for (int i = 0; i < V; ++i) {
            if (visited.find(i) == visited.end()) {
                dfs(i, in_degree, visited, adj);
            }
        }

        int odd_degrees = 0;

        for (int i = 0; i < V; ++i) {
            if (in_degree[i] % 2 != 0) {
                odd_degrees++;
            }
        }

        if (odd_degrees == 0) {
            return 2;  // Eulerian Circuit
        } else if (odd_degrees == 2) {
            return 1;  // Eulerian Path
        } else {
            return 0;  // No Eulerian Path or Circuit
        }
    }
};


//{ Driver Code Starts.
int main(){
	int tc;
	cin >> tc;
	while(tc--){
		int V, E;
		cin >> V >> E;
		vector<int>adj[V];
		for(int i = 0; i < E; i++){
			int u, v;
			cin >> u >> v;
			adj[u].push_back(v);
			adj[v].push_back(u);
		}
		Solution obj;
		int ans = obj.isEulerCircuit(V, adj);
		cout << ans <<"\n";	}
	return 0;
}
// } Driver Code Ends