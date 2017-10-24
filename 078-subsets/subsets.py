# -*- coding:utf-8 -*-


#
# Given a set of distinct integers, nums, return all possible subsets (the power set).
#
# Note: The solution set must not contain duplicate subsets.
#
#
# For example,
# If nums = [1,2,3], a solution is:
#
#
#
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # iterative
        
        res = [[]]
        
        for n in nums:
            res += [item + [n] for item in res]
        return res
        
