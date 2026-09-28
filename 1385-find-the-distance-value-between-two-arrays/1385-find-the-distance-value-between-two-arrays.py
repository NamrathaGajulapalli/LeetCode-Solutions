class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        x=0
        for i in arr1:
            c=0
            for j in arr2:
                if abs(i-j)>d:
                    c+=1
            if c==len(arr2):
                x+=1
        return x                

        