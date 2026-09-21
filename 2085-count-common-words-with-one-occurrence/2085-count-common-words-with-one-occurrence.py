class Solution:
    def countWords(self, words1: list[str], words2: list[str]) -> int:
        d1={}
        d2={}
        c=0
        x=[]
        y=[]
        for i in words1:
            if i in d1:
                d1[i]+=1
            else:
                d1[i]=1
        for i in words2:
            if i in d2:
                d2[i]+=1
            else:
                d2[i]=1        
        for i in d1:
            if d1[i]==1:
                x.append(i)
        for i in d2:
            if d2[i]==1:
                y.append(i)
        for i in x:
            if i in y:
                c+=1
        return c                         
                              
        