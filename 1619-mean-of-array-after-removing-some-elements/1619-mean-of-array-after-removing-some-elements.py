class Solution:
    def trimMean(self, arr: list[int]) -> float:
        n=len(arr)
        x=(n*5)//100
        arr=sorted(arr)
        arr=arr[x:n-x]
        y=len(arr)
        mean=sum(arr)/y
        return mean

        