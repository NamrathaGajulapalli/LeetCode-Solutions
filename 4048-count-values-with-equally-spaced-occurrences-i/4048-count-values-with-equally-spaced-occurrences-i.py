class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        c=0
        for i in nums:
            if nums.count(i)==3:
                i1=nums.index(i)
                i2=nums.index(i,i1+1)
                i3=nums.index(i,i2+1)
                if i2-i1==i3-i2:
                    c+=1
        return c//3            
        