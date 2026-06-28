class Solution:
    def maxSum(self, nums: list[int], k: int, mul: int) -> int:
        nums.sort(reverse=True)
        ans=0

        for i in range(k):
            ans+=nums[i]*max(mul-i,1)

        return ans