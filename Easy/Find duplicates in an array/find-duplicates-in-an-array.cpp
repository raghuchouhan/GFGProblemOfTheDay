//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<int> duplicates(long long arr[], int n) {
        unordered_map<int, int> map;
        vector<int> ans;

        // Inserting elements into the map
        for (int i = 0; i < n; i++) {
            map[arr[i]]++;
        }

        // If more than 1 count, push the element into the answer vector
        for (auto i : map) {
            if (i.second > 1) {
                ans.push_back(i.first);
            }
        }

        // If no repetition, push -1 into the vector and return
        if (ans.empty()) {
            ans.push_back(-1);
            return ans;
        } else {
            // Output required as sorted, so sorting the vector
            sort(ans.begin(), ans.end());
            return ans;
        }
    }
};


//{ Driver Code Starts.
int main() {
    int t;
    cin >> t;
    while (t-- > 0) {
        int n;
        cin >> n;
        long long a[n];
        for (int i = 0; i < n; i++) cin >> a[i];
        Solution obj;
        vector<int> ans = obj.duplicates(a, n);
        for (int i : ans) cout << i << ' ';
        cout << endl;
    }
    return 0;
}

// } Driver Code Ends