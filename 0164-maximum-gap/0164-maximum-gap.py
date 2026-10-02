class Solution:
    def maximumGap(self, nums: list[int]) -> int:
        nums=sorted(nums)
        maxi=0
        for i in range(1,len(nums)):
            x=abs(nums[i]-nums[i-1])
            if x>maxi:
                maxi=x
        return maxi            
        