class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        l=list(words)
        r=[]
        for i in words:
            r.append(' ')
            for j in i:
                if j==separator:
                    r.append(' ')
                else:
                    r.append(j)
        return ''.join(r).split()           
                      

        