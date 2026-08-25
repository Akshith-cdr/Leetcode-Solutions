class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        hset=set(nums)

        multiple=k

        while multiple in hset:
            multiple+=k
        
        return multiple