class Solution:
    def maximumDifference(self, nums: list[int]) -> int:
        maxi=[]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if j>i and nums[i]<nums[j]:
                    maxi.append(nums[j]-nums[i])
        if maxi:
            return max(maxi)
        return -1        
        