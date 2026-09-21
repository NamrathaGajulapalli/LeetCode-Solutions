class Solution:
    def largestGoodInteger(self, num: str) -> str:
        r=[]
        for i in range(1,len(num)-1):
            if num[i-1]==num[i]==num[i+1]:
                r.append(str(num[i]))
        if r:
            return str(max(r))*3
        return ''            
        