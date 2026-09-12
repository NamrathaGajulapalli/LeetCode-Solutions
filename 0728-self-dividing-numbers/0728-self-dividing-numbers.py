class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        l=[]
        for i in range(left,right+1):
            s=list(str(i))
            sz=len(s)
            c=0
            for j in range(sz):
                if int(s[j])==0:
                    break
                if i%int(s[j])==0:
                    c+=1
            if c==sz:
                l.append(i)   
        return l          
        