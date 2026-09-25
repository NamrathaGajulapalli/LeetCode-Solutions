class Solution:
    def calPoints(self, operations: list[str]) -> int:
        l=[]
        for i in operations:
            if i=='+':
                l.append(int(l[-1])+int(l[-2]))
            elif i=='C':
                l.pop()
            elif i=='D':
                l.append(int(l[-1])*2)
            else:
                l.append(int(i))
        return sum(l)                    
        