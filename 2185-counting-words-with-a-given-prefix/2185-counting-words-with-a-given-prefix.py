class Solution:
    def prefixCount(self, words: list[str], pref: str) -> int:
        c=0
        x=len(pref)
        for i in words:
            if i[:x]==pref:
                c+=1
        return c        
        