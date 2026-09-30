class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        d={}
        l=[]
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i,j in d.items():
            if j>(len(nums)/3):
                l.append(i)  
        return l                  
        