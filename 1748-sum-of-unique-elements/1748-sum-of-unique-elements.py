class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        d={}
        sumi=0
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i,j in d.items():
            if j==1:
                sumi+=i
        return sumi                
                    
        