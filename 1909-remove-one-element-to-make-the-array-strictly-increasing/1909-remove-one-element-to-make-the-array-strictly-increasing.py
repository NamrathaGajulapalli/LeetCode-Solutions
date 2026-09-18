class Solution:
    def canBeIncreasing(self, nums: list[int]) -> bool:
        temp=nums.copy()
        for i in range(len(nums)):
            temp.pop(i)
            c=0
            for j in range(len(temp)-1):
                if temp[j]<temp[j+1]:
                    c+=1
            if c==len(nums)-2:
                return True               
            temp=nums.copy()
        return False            
                    


        