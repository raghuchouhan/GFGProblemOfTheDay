//{ Driver Code Starts
//Initial Template for C++

#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
//User function Template for C++

#include <iostream>
using namespace std;

class Solution {
public:
    int singleElement(int arr[], int N) {
        int result = 0;

        // Iterate through all bits
        for (int i = 0; i < 32; i++) {
            // Count the number of set bits at the current position
            int count = 0;
            for (int j = 0; j < N; j++) {
                if (arr[j] & (1 << i)) {
                    count++;
                }
            }

            // Take modulus by 3 to get the bit of the element that occurs once
            count %= 3;

            // Set the bit in the result
            result |= (count << i);
        }

        return result;
    }
};




//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {
        int N;
        
        cin>>N;
        int arr[N];
        
        for(int i=0 ; i<N ; i++)
            cin>>arr[i];

        Solution ob;
        cout<<ob.singleElement(arr,N);
        cout<<"\n";
    }
    return 0;
}
// } Driver Code Ends