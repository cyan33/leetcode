# -*- coding:utf-8 -*-


# Given an array of integers, 1 &le; a[i] &le; n (n = size of array), some elements appear twice and others appear once.
#
# Find all the elements that appear twice in this array.
#
# Could you do it without extra space and in O(n) runtime?
#
# Example:
#
# Input:
# [4,3,2,7,8,2,3,1]
#
# Output:
# [2,3]


class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dic = {}
        res = []
        for i in nums:
            if str(i) in dic:
                res.append(i)
            dic[str(i)] = i
        return res

