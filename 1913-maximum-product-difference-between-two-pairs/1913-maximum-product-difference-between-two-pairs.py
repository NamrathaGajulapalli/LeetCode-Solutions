class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        # my code
        # nums.sort()
        # return (nums[-1]*nums[-2])-(nums[0]*nums[1])
        a=max(nums)
        nums.remove(a)
        b=max(nums)
        nums.remove(b)
        c=min(nums)
        nums.remove(c)
        d=min(nums)
        return (a*b)-(c*d)