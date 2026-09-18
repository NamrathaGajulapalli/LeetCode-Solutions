class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        n=float('inf')
        i=1
        x=0
        while i<n:
            if i not in arr:
                x+=1
                if x==k:
                    return i
            i+=1        


        