class Solution:
    def findSpecialInteger(self, arr: list[int]) -> int:
        d={}
        for i in arr:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i,j in d.items():
            if (j*100)/len(arr)>25:
                return i            

        