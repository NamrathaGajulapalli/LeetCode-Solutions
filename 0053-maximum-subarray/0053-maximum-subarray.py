class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # maxi=float('-inf')
        # for i in range(len(nums)):
        #     sum=0
        #     for j in range(i,len(nums)):
        #         sum+=nums[j]
        #         maxi=max(maxi,sum)
        # return maxi 
        ss=0
        ts=min(nums)
        for i in nums:
            ss+=i
            if ss>ts:
                ts=ss
            if ss<0:
                ss=0
        return ts                   


        # cs=0
        # gs=float("-inf")
        # for i in nums:
        #     cs=cs+i
        #     if cs>gs:
        #         gs=cs
        #     if cs<0:
        #         cs=0
        # return gs        
        