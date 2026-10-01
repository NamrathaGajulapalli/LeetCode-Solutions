class Solution:
    def canThreePartsEqualSum(self, arr: list[int]) -> bool:
        # if all(x==0 for x in arr):
        #     return True
        if sum(arr)%3!=0:
            return False
        ps=sum(arr)//3
        x=0
        c=0
        for i in arr:
            x+=i
            if x==ps:
                c+=1
                x=0
        if c>=3:
            return True
        return False            



        