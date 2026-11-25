class Solution:
    def numberOfPairs(self, nums: list[int]) -> list[int]:
        temp=nums.copy()
        c=0
        for i in temp:
            if nums.count(i)>=2:
                nums.remove(i)
                nums.remove(i)
                c+=1
        return [c,len(nums)]        
        
        