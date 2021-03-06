#
# @lc app=leetcode id=349 lang=python
#
# [349] Intersection of Two Arrays
#
class Solution(object):
    # Hash Table
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        def performMap(nums):
            dict = {}
            for i in nums:
                if not dict.get(i):
                    dict[i] = 1
            return dict

        len1, len2 = len(nums1), len(nums2)
        inter = {}
        if len1 < len2:
            dict = performMap(nums1)
            for j in nums2:
                if dict.get(j):
                    inter[j] = 1
        else:
            dict = performMap(nums2)
            for j in nums1:
                if dict.get(j):
                    inter[j] = 1
        return list(inter.keys())

