class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        l=[]
        for i,j in d.items():
            if j>2:
                l.extend([i]*2)
            else:
                l.extend([i]*j)
        x=len(l)        
        l.extend(['-']*(len(nums)-x))
        nums[:]=l
        return x
                                 
        