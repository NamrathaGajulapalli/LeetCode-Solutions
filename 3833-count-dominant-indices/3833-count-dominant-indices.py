import statistics
class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        c=0
        sn=sum(nums)
        ti=len(nums)
        for i in range(len(nums)):
            if i==len(nums)-1:
                break
            sn=sn-nums[i]
            ti=ti-1
            if nums[i]>sn//ti:
                c+=1
        return c        





        # n=len(nums)
        # c=0
        # for i in range(n):
        #     if i==n-1:
        #         break
        #     if nums[i]>statistics.mean(nums[i+1:n]):
        #         c+=1
        # return c        
