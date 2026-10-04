class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        d={}
        for i in range(len(mat)):
            d[i]=mat[i].count(1)
        maxi=max(d.values())
        for i,j in d.items():
            if j==maxi:
                return [i,j]   
