class Solution:
    def findFinalValue(self, nums: list[int], original: int) -> int:
        r=0
        while True:
            if original in nums:
                r=original*2
                original=r
            else:
                break
        if r==0:
            return original        
        return r            
                

        