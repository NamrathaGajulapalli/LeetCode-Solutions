class Solution:
    def minMergedInteger(self, nums: list[int]) -> int:
        l=[]
        i=0
        while i<len(nums):
            l.append(int(str(nums[i])+str(nums[i+1])))
            i+=2
        return min(l)    
            
        