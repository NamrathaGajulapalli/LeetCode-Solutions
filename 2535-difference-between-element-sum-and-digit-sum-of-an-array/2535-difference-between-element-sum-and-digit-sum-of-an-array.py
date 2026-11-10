class Solution:
    def differenceOfSum(self, nums: list[int]) -> int:
        x=sum(nums)
        sumi=0
        for i in nums:
            temp=i
            while temp>0:
                n=temp%10
                sumi+=n
                temp=temp//10
        return abs(x-sumi)        

        