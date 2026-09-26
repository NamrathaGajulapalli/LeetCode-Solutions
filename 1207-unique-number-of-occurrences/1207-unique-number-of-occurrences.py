class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        d={}
        for i in arr:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        s=[]            
        for i in d:
            s.append(d[i])
        return len(s)==len(set(s))           
                   
        