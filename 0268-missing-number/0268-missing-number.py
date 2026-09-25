class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        x=(n*(n+1))/2
        s=sum(nums)
        return int(x-s)
        # for i in range(len(nums)+1):
        #     if i not in nums:
        #         return i

        