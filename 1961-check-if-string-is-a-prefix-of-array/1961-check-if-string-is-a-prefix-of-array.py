class Solution:
    def isPrefixString(self, s: str, words: list[str]) -> bool:
        r=''
        for i in range(len(words)):
            r+=words[i]
            if r==s:
                return True
        return False        


        