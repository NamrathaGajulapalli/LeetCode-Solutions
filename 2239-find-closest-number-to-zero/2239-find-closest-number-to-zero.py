class Solution:
    def findClosestNumber(self, nums: list[int]) -> int:
        l=[]
        nums=sorted(nums)
        r=nums[::-1]
        for i in r:
            l.append(abs(i-0))
        m=l.index(min(l))
        return r[m]    
           

        