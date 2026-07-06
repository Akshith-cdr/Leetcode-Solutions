class Solution:
    def canMakeSubsequence(self, s: str, t: str) -> bool:
        n,m=len(s),len(t)
        
        if n>m:
            return False
        
        if n==0:
            return True
        
        left=[m]*n
        j=0
        for i in range(n):
            while j<m and t[j]!=s[i]:
                j+=1
            
            if j==m:
                break
            
            left[i]=j
            j+=1
        
        if left[-1]<m:
            return True
        
        nxt=m
        j=m-1
        for i in range(n-1,-1,-1):
            while j>=0 and t[j]!=s[i]:
                j-=1
            
            l=left[i-1] if i else -1
            
            if l+1<nxt:
                return True
            
            if j<0:
                break
            
            nxt=j
            j-=1
        
        return False