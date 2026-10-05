class Solution:
    def scoreOfString(self, s: str) -> int:
        sumi=0
        for i in range(1,len(s)):
            sumi+=abs(ord(s[i])-ord(s[i-1]))
        return sumi   

        