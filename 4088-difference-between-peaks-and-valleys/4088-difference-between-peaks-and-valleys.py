class Solution:
    def peakValleyDifference(self, nums: list[int]) -> int:
        p=0
        v=0
        i=1
        while i<len(nums)-1:
            if nums[i-1]<nums[i]>nums[i+1]:
                p+=nums[i]
            elif nums[i-1]>nums[i]<nums[i+1]:
                v+=nums[i]
            i+=1    
        return p-v             
        