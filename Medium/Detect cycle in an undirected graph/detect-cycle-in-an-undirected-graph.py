from typing import List

class Solution:
    # Function to detect cycle in an undirected graph.
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        # Helper function to perform DFS and check for cycles.
        def dfs(node, parent, visited):
            visited[node] = True

            # Traverse the neighbors of the current node.
            for neighbor in adj[node]:
                # If the neighbor is not visited, recursively call DFS.
                if not visited[neighbor]:
                    if dfs(neighbor, node, visited):
                        return True
                # If the neighbor is visited and not the parent of the current node,
                # then a cycle is detected.
                elif neighbor != parent:
                    return True

            return False

        # Initialize visited array.
        visited = [False] * V

        # Iterate through all vertices and check for cycles.
        for vertex in range(V):
            if not visited[vertex]:
                if dfs(vertex, -1, visited):
                    return True

        return False


#{ 
 # Driver Code Starts

if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends