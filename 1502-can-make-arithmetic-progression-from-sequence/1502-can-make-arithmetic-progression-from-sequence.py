class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        s=sorted(arr)
        x=s[1]-s[0]
        for i in range(len(s)-1):
            if s[i+1]-s[i]!=x:
                return False
        return True        
                        

        