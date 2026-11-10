class Solution:
    def minMovesToSeat(self, seats: list[int], students: list[int]) -> int:
        seats.sort()
        students.sort()
        t=0
        for i in range(len(seats)):
            t+=abs(students[i]-seats[i])
        return t    

        