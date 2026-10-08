class Solution:
    def mostFrequentEven(self, nums: list[int]) -> int:
        e=[]
        for i in nums:
            if i%2==0:
                e.append(i)
        e=sorted(e)
        d={}
        for i in e:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        if d:        
            maxi=max(d.values())
        for i,j in d.items():
            if j==maxi:
                return i
        return -1                    
            

        