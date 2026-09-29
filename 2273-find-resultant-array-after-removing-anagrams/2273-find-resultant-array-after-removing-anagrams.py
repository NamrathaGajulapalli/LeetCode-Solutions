class Solution:
    def removeAnagrams(self, words: list[str]) -> list[str]:
        r=[words[0]]
        for i in range(1,len(words)):
            x=''.join(sorted(words[i]))
            y=''.join(sorted(words[i-1]))
            if x!=y:
                r.append(words[i])
        return r        
        