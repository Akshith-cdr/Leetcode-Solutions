class Solution:
    def countTime(self, time: str) -> int:
        ans=1
        h1,h2,_,m1,m2=time
        
        if h1=="?" and h2=="?":
            ans*=24
        elif h1=="?":
            if int(h2)>=4:
                ans*=2
            else:
                ans*=3
                
        elif h2=="?":
            if int(h1)<=1:
                ans*=10
            elif h1=="2":
                ans*=4
                
        if m1=="?" and m2=="?":
            ans*=60
        elif m1=="?":
            ans*=6
        elif m2=="?":
            ans*=10
        
        return ans