class Solution:
    def divideArray(self, nums: list[int]) -> bool:
        if len(nums)%2!=0:
            return False
        f=True  
        d={}  
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i,j in d.items():
            if j%2!=0:
                f=False        


        return f        

        