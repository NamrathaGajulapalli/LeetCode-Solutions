class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        s1=set(nums1)
        s2=set(nums2)
        return [list(s1-s2),list(s2-s1)]

        # a=set()
        # b=set()
        # for i in range(len(nums1)):
        #     if nums1[i] not in nums2:
        #         a.add(nums1[i])
        # for i in range(len(nums2)):
        #     if nums2[i] not in nums1:
        #         b.add(nums2[i]) 
        # r=[]
        # r.append(list(a))
        # r.append(list(b))
        # return r               

        