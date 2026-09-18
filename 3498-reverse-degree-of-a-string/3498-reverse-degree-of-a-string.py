class Solution:
    def reverseDegree(self, s: str) -> int:
        sum=0
        for i in range(len(s)):
            x=123-ord(s[i])
            sum+=x*(i+1)
        return sum

        