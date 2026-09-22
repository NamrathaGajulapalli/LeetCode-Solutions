class Solution:
    def busyStudent(self, startTime: list[int], endTime: list[int], queryTime: int) -> int:
        c=0
        for i in range(len(startTime)):
            if startTime[i]<=queryTime<=endTime[i]:
                c+=1
        return c        

        