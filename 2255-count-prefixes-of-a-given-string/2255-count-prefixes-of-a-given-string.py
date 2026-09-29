class Solution:
    def countPrefixes(self, words: list[str], s: str) -> int:
        c=0
        for i in words:
            l=len(i)
            if i==s[:l]:
                c+=1
        return c        

        