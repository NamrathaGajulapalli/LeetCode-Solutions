class Solution:
    def reverseDegree(self, s: str) -> int:
        sum=0
        for i in range(len(s)):
            x=abs(ord(s[i])-123)
            sum+=x*(i+1)
        return sum

        