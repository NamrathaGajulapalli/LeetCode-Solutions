class Solution:
    def minimumDifference(self, nums: list[int], k: int) -> int:
        nums.sort()
        l=[]
        for i in range(len(nums)-k+1):
            l.append(abs(nums[i]-nums[i+k-1]))
        if l:
            return min(l)
        return 0        
