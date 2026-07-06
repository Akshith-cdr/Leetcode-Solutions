class Solution(object):
    def maxDigitRange(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ranges=[]

        for num in nums:
            s=str(num)
            ranges.append(int(max(s))-int(min(s)))

        m=max(ranges)
        ans=0

        for i in range(len(nums)):
            if ranges[i]==m:
                ans+=nums[i]

        return ans