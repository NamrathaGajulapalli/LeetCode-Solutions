class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        c=0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i==j:
                    continue
                if 0<=i<j<len(nums) and nums[i]+nums[j]<target:
                    c+=1
        return c            



        