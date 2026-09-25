class Solution:
    def calPoints(self, operations: list[str]) -> int:
        l=[]
        for i in range(len(operations)):
            if operations[i]=='+':
                l.append(int(l[-1])+int(l[-2]))
            elif operations[i]=='C':
                l.pop()
            elif operations[i]=='D':
                l.append(int(l[-1])*2)
            else:
                l.append(int(operations[i]))
        return sum(l)                    
        