class Solution:
    def countRotations(self, s: str, k: int) -> int:
        n=len(s)
        ep=0

        for i in range(n):
            if s[i]==s[(i+1)%n]:
                ep+=1
        
        tot=ep

        if k==tot-1:
            return ep
        if k==tot:
            return n-ep
        
        return 0