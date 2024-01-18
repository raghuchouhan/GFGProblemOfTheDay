from typing import List

class Solution:
    def wordBreak(self, n: int, dict: List[str], s: str) -> List[str]:
        def word_break_helper(start, current_sentence, result):
            if start == len(s):
                result.append(' '.join(current_sentence))
                return
            
            for end in range(start + 1, len(s) + 1):
                current_word = s[start:end]
                if current_word in dict:
                    word_break_helper(end, current_sentence + [current_word], result)
        
        result = []
        word_break_helper(0, [], result)
        return result


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        dicti = input().split()
        s = input()
        
        ob = Solution()
        ans = ob.wordBreak(n, dicti, s)
        if(len(ans) == 0):
            print("Empty")
        else:
            ans.sort()
            for it in (ans):
                print("("+it,end = ")")
            print()
# } Driver Code Ends