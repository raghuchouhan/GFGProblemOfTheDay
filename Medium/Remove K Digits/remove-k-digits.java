//{ Driver Code Starts
// Initial Template for Java

import java.io.*;
import java.util.*;

class GfG {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while (t-- > 0) {
            String S = sc.next();
            int K = sc.nextInt();
            Solution obj = new Solution();
            System.out.println(obj.removeKdigits(S, K));
        }
    }
}

// } Driver Code Ends


// User function Template for Java

class Solution {
    public String removeKdigits(String S, int k) {
        // code here
        
        Stack<Character> st=new Stack();
        
        for(char c:S.toCharArray())
        {
            while(k>0 && !st.isEmpty() && st.peek()>c)
            {
                st.pop();
                k--;
            }
            if(!st.isEmpty() || c!='0')
            st.push(c);
            
        }
        while(!st.isEmpty() && k>0)
        {
            st.pop();
            k--;
        }
        //System.out.println(st);
        StringBuilder ans=new StringBuilder("");
        while(!st.isEmpty())
        {
            ans=ans.append(st.pop());
        }
        String a=ans.reverse().toString();
        if(a.equals(""))
        return "0";
        return a;
    }
}