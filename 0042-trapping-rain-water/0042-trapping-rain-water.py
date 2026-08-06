class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n=len(height)
        l,r=0,n-1
        maxl,maxr=0,0
        tot=0

        while l<=r:
            if height[l]<=height[r]:
                if height[l]>=maxl:
                    maxl=height[l]
                else:
                    tot+=maxl-height[l]
                
                l+=1
            else:
                if height[r]>=maxr:
                    maxr=height[r]
                else:
                    tot+=maxr-height[r]
                
                r-=1
        
        return tot