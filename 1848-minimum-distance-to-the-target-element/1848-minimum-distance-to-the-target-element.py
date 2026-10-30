class Solution:
    def getMinDistance(self, nums: list[int], target: int, start: int) -> int:
        mini=len(nums)
        for i in range(len(nums)):
            if nums[i]==target:
                x=abs(start-i)
                mini=min(mini,x)
        return mini        


        