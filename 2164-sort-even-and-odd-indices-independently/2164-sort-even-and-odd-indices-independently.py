class Solution:
    def sortEvenOdd(self, nums: list[int]) -> list[int]:
        o=[]
        e=[]
        r=[]
        for i in range(len(nums)):
            if i%2==0:
                e.append(nums[i])
            else:    
                o.append(nums[i])
        o=sorted(o)
        e=sorted(e)
        ei=0
        for i in range(len(nums)):
            if i%2!=0:
                r.append(o.pop())
            else:
                r.append(e[ei])
                ei+=1
        return r                   

        