class Solution:
    def rob(self, nums: list[int]) -> int:
        sumi1=0
        sumi2=0
        for i in nums:
            sumi1,sumi2=sumi2,max(sumi2,sumi1+i)
        return sumi2    
   
        