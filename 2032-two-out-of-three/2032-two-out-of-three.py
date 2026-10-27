class Solution:
    def twoOutOfThree(self, nums1: list[int], nums2: list[int], nums3: list[int]) -> list[int]:
        r=set()
        for i in nums1:
            if i in nums2 or i in nums3:
                r.add(i)
        for i in nums2:
            if i in nums1 or i in nums3:
                r.add(i)
        for i in nums3:
            if i in nums2 or i in nums1:
                r.add(i) 
        return list(r)                      


        