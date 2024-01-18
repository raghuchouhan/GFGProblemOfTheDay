//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// Tree Node
struct Node {
    int data;
    Node *left;
    Node *right;

    Node(int val) {
        data = val;
        left = right = NULL;
    }
};

// Function to Build Tree
Node *buildTree(string str) {
    // Corner Case
    if (str.length() == 0 || str[0] == 'N') return NULL;

    // Creating vector of strings from input
    // string after spliting by space
    vector<string> ip;

    istringstream iss(str);
    for (string str; iss >> str;) ip.push_back(str);

    // Create the root of the tree
    Node *root = new Node(stoi(ip[0]));

    // Push the root to the queue
    queue<Node *> queue;
    queue.push(root);

    // Starting from the second element
    int i = 1;
    while (!queue.empty() && i < ip.size()) {

        // Get and remove the front of the queue
        Node *currNode = queue.front();
        queue.pop();

        // Get the current Node's value from the string
        string currVal = ip[i];

        // If the left child is not null
        if (currVal != "N") {

            // Create the left child for the current Node
            currNode->left = new Node(stoi(currVal));

            // Push it to the queue
            queue.push(currNode->left);
        }

        // For the right child
        i++;
        if (i >= ip.size()) break;
        currVal = ip[i];

        // If the right child is not null
        if (currVal != "N") {

            // Create the right child for the current Node
            currNode->right = new Node(stoi(currVal));

            // Push it to the queue
            queue.push(currNode->right);
        }
        i++;
    }

    return root;
}


// } Driver Code Ends
class Solution 
{
    int maxSum;
   
    int solve(Node *root, Node *mainroot)
    {
        
        // if(root == nullptr) return INT_MIN;
        //we get a leaf
        if(root->left == nullptr && root->right == nullptr)
        {
            return root->data;
        }
        int takeLeft = 0;
        int takeRight = 0;
        if(root->left) takeLeft = solve(root->left, mainroot);
        if(root->right) takeRight = solve(root->right, mainroot);
        int takeRoot = takeLeft + takeRight + root->data;

        int maxi = takeRoot;
        
        //case when root has left null (then root can be our special node)
        if(root == mainroot && (maxi > maxSum))  maxSum = maxi;
        
        if(root->left && root->right)
        {
            if( (maxi > maxSum)) maxSum = maxi;
        }
        if(!root->left) return takeRoot;
        if(!root->right) return takeRoot;
        
        return max(takeLeft + root->data, takeRight + root->data);
        // return takeRoot;
    }
    public:
    Solution()
    {
        maxSum = INT_MIN;
    }
    int maxPathSum(Node* root)
    {
        if(root == nullptr) return 0;
        if(root->left == nullptr && root->right == nullptr) return root->data;
        if(root->left && root->right)
        if(root->left->left == nullptr && root->left->right == nullptr && root->right->left == nullptr && root->right->right == nullptr)
        {
            return root->left->data + root->data + root->right->data;
        }
        Node *mainroot = root;
        solve(root, mainroot);
        return maxSum;
    }
};



//{ Driver Code Starts.

int main() {
    int tc;
    scanf("%d ", &tc);
    while (tc--) {
        string treeString;
        getline(cin, treeString);
        Node *root = buildTree(treeString);
        Solution ob;
        cout << ob.maxPathSum(root) << "\n";
    }
    return 0;
}
// } Driver Code Ends