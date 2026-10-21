class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        r=[]
        order=["electronics", "grocery", "pharmacy", "restaurant"]
        for i in range(len(code)):
            t=True
            if len(code[i])==0:
                continue
            for j in range(len(code[i])):
                if code[i][j].isalnum() or code[i][j]=='_':
                    continue
                else:
                    t=False
            if t and isActive[i]==True and businessLine[i] in order:
                r.append((order.index(businessLine[i]),code[i]))
        r.sort()
        x=[]
        for i in r:
            x.append(i[1])
        return x    




        