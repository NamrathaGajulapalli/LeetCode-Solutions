class Solution:
    def divideArray(self, nums: list[int]) -> bool:
        if len(nums)%2!=0:
            return False
        f=True    
        for i in nums:
            if nums.count(i)%2!=0:
                f=False
        return f        

        