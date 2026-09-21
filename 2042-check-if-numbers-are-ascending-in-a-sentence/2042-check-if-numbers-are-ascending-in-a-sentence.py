class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        l=list(s.split(' '))
        x=[]
        for i in l:
            if i.isdigit():
                x.append(int(i))
        flag=True      
        for i in range(len(x)-1):
            if x[i]>=x[i+1]:
                flag=False
        return flag           
                
                
           
        #     if i.isdigit():
        #         l.append(i)
        # return sorted(l)        
        