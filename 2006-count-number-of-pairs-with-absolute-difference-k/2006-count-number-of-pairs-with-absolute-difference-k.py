class Solution:
    def countKDifference(self, nums: list[int], k: int) -> int:
        c=0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i==j:
                    continue
                if nums[i]-nums[j]==k:
                    c+=1
        return c                
        