class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        l=0
        r=0
        mini=float('inf')
        sumi=0
        while r<len(nums):
            sumi+=nums[r]
            r+=1
            while sumi>=target:
                length=r-l
                mini=min(length,mini)
                sumi-=nums[l]
                l+=1     
        if mini==float('inf'):
            return 0
        return mini    
            