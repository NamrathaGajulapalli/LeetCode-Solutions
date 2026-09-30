class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        n=len(nums)
        d={}
        l=[]
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i,j in d.items():
            if j>(n/3):
                l.append(i)  
        return l                  
        