class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        sumi=0
        for i in range(len(s)):
            sumi+=abs(i-t.index(s[i]))
        return sumi    
        