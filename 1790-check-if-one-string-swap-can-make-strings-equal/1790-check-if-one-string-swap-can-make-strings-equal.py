class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1==s2:
            return True
        l=[]
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                l.append(i)
        if len(l)!=2:
            return False
        s1=list(s1)
        s2=list(s2)
        s1[l[0]],s1[l[1]]=s1[l[1]],s1[l[0]]
        if s1==s2:
            return True
        s2[l[0]],s2[l[1]]=s2[l[1]],s2[l[0]] 
        if s1==s2:
            return True 
        return False      

            


            
