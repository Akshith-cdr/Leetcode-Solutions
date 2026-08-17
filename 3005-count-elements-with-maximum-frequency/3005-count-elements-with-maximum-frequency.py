class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq=[0]*101
        maxf=0

        for n in nums:
            freq[n]+=1
            maxf=max(maxf,freq[n])

        ans=0
        for f in freq:
            if f==maxf:
                ans+=f
        
        return ans