class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        r=''
        for i in range(len(s)):
            r+=s[(k+i)%len(s)]
        return r            
        