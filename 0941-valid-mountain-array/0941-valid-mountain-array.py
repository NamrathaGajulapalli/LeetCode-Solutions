class Solution:
    def validMountainArray(self, arr: list[int]) -> bool:
        if len(arr)<3:
            return False   
        f=True
        maxi=max(arr)
        ind=arr.index(maxi)
        if ind==0 or ind==len(arr)-1:
            return False
        if arr[ind]==arr[ind-1] or arr[ind]==arr[ind+1]:
            return False    
        for i in range(1,ind):
            if arr[i-1]>=arr[i]:
                f=False
        for i in range(ind+1,len(arr)):
            if arr[i-1]<=arr[i]:
                f=False
        return f            



        # for i in arr:
        #     if arr.count(i)>1:
        #         return False
        # if len(arr)<3:
        #     return False
        # x=arr.index(max(arr))
        # f=True
        # y=0
        # for i in range(x):
        #     if arr[i]>arr[i+1]:
        #         f=False
        #     else:    
        #         y+=1
        # g=True  
        # z=0      
        # for i in range(x,len(arr)-1):
        #     if arr[i]<arr[i+1]: 
        #         g=False
        #     else:    
        #         z+=1
        # return f and g and y>0 and z>0              



            


        