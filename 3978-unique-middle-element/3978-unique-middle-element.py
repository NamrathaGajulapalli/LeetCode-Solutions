class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        x=nums[len(nums)//2]
        c=0
        for i in nums:
            if i==x:
                c+=1
        if c==1:
            return True
        return False            
        