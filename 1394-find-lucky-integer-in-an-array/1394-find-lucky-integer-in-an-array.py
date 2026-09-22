class Solution:
    def findLucky(self, arr: list[int]) -> int:
        d={}
        l=[]
        for i in arr:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i,j in d.items():
            if i==j:
                l.append(i)
        if l:
            return max(l)
        return -1                       
        