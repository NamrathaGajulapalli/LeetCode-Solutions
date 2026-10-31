class Solution:
    def countPairs(self, nums: list[int], k: int) -> int:
        c=0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i==j:
                    continue
                if 0<=i<j<len(nums) and nums[i]==nums[j] and ((i*j)%k==0 or (i*j)==0):
                    c+=1 
        return c              
        