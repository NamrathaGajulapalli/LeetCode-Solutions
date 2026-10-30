class Solution:
    def averageValue(self, nums: list[int]) -> int:
        sumi=0
        c=0
        for i in nums:
            if i%6==0:
                sumi+=i
                c+=1
        if c==0:
            return 0        
        return sumi//c       
        