class Solution:
    def findMiddleIndex(self, nums: list[int]) -> int:
        if all(x==0 for x in nums):
            return 0
        if len(nums)==1:
            return 0
        if len(nums)==2:
            if nums[1]==0:
                return 0    
        for i in range (len(nums)):
            s1=sum(nums[:i])
            s2=sum(nums[i+1:])
            if s1==s2:
                return i
        return -1            

        
               
                

        