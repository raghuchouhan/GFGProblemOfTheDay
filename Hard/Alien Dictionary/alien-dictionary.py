from collections import defaultdict, deque

class Solution:
    def findOrder(self, alien_dict, N, K):
        graph = defaultdict(list)
        in_degree = {char: 0 for char in set("".join(alien_dict))}
        
        # Build the graph and calculate in-degrees
        for i in range(N - 1):
            word1, word2 = alien_dict[i], alien_dict[i + 1]
            min_len = min(len(word1), len(word2))
            
            for j in range(min_len):
                if word1[j] != word2[j]:
                    graph[word1[j]].append(word2[j])
                    in_degree[word2[j]] += 1
                    break
        
        # Perform topological sort using BFS
        queue = deque([char for char in in_degree if in_degree[char] == 0])
        result = []
        
        while queue:
            current_char = queue.popleft()
            result.append(current_char)
            
            for neighbor in graph[current_char]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # Check if there is a cycle in the graph
        if len(result) != len(set("".join(alien_dict))):
            return ""  # Invalid order, return empty string
        
        return "".join(result)






#{ 
 # Driver Code Starts
#Initial Template for Python 3

class sort_by_order:
    def __init__(self,s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i
    
    def transform(self,word):
        new_word = ''
        for c in word:
            new_word += chr( ord('a') + self.priority[c] )
        return new_word
    
    def sort_this_list(self,lst):
        lst.sort(key = self.transform)

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        line=input().strip().split()
        n=int(line[0])
        k=int(line[1])
        
        alien_dict = [x for x in input().strip().split()]
        duplicate_dict = alien_dict.copy()
        ob=Solution()
        order = ob.findOrder(alien_dict,n,k)
        s = ""
        for i in range(k):
            s += chr(97+i)
        l = list(order)
        l.sort()
        l = "".join(l)
        if s != l:
            print(0)
        else:
            x = sort_by_order(order)
            x.sort_this_list(duplicate_dict)
            
            if duplicate_dict == alien_dict:
                print(1)
            else:
                print(0)


# } Driver Code Ends