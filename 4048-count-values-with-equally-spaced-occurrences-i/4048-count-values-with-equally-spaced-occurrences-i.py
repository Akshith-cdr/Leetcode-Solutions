class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        pos=defaultdict(list)
        
        for i,x in enumerate(nums):
            pos[x].append(i)
        
        ans=0
        
        for x,ind in pos.items():
            if len(ind)==3:
                i1,i2,i3=ind
                if(i2-i1)==(i3-i2):
                    ans+=1
        
        return ans