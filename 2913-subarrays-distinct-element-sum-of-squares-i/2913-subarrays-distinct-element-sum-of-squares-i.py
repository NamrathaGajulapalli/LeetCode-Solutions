class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        l=[]
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                l.append(len(set(nums[i:j+1])))
        sumi=0
        for i in l:
            sumi+=i*i
        return sumi            
        