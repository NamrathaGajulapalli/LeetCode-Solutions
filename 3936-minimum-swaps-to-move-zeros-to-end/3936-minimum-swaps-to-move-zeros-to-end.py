class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        s=nums.count(0)
        c=0
        for i in range(len(nums)-s):
            if nums[i]==0:
                c+=1
        return c        

        