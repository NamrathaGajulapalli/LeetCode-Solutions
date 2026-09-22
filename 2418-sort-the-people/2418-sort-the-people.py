class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        h=sorted(heights)[::-1]
        l=[]
        for i in h:
            x=heights.index(i)
            l.append(names[x])
        return l     
        