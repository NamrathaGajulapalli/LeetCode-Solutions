class Solution:
    def maximumUnits(self, boxTypes: list[list[int]], truckSize: int) -> int:
        c=0
        boxTypes.sort(key=lambda x:x[1],reverse=True)
        for i in range(len(boxTypes)):
            if boxTypes[i][0]<truckSize:
                c+=boxTypes[i][0]*boxTypes[i][1]
                truckSize-=boxTypes[i][0]
            elif truckSize>0:
                c+=boxTypes[i][1]*truckSize
                break
        return c            



     
        