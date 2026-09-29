class Solution:
    def sortArrayByParityII(self, nums: list[int]) -> list[int]:
        i=0
        a=[]
        b=[]
        r=[]
        for i in nums:
            if i%2==0:
                a.append(i)
            else:
                b.append(i)
        for i in range(len(nums)//2):
            r.append(a[i])
            r.append(b[i])  
        return r             
