class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        i=sorted(nums)
        d=i[::-1]
        return nums==i or nums==d
        