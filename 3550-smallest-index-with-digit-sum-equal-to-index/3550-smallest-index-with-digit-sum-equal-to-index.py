class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        l=0
        for i in range(len(nums)):
            n=nums[i]
            s=0
            while n>0:
                d=n%10
                s+=d
                n//=10
            if i==s:
                return i    
        return -1        
        