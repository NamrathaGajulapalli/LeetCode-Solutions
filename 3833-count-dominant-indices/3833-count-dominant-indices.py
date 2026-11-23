import statistics
class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        n=len(nums)
        c=0
        for i in range(n):
            if i==n-1:
                break
            if nums[i]>statistics.mean(nums[i+1:n]):
                c+=1
        return c        
