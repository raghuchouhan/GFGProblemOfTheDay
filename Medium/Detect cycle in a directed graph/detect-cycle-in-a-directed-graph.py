from collections import defaultdict

class Solution:
    def isCyclic(self, V, adj):
        def dfs(node, visited, stack):
            visited[node] = True
            stack[node] = True

            for neighbor in adj[node]:
                if not visited[neighbor]:
                    if dfs(neighbor, visited, stack):
                        return True
                elif stack[neighbor]:
                    return True

            stack[node] = False
            return False

        visited = [False] * V
        stack = [False] * V

        for node in range(V):
            if not visited[node]:
                if dfs(node, visited, stack):
                    return True

        return False


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)
        
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V,E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a,b = map(int,input().strip().split())
            adj[a].append(b)
        ob = Solution()
        
        if ob.isCyclic(V, adj):
            print(1)
        else:
            print(0)
# } Driver Code Ends