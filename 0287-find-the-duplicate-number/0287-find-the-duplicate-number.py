class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        d=set()
        for i in nums:
            if i in d:
                return i
            else:
                d.add(i)    
        # x=sum(nums)
        # y=sum(set(nums))
        # return x-y        
        