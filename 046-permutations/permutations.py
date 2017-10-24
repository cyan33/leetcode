# -*- coding:utf-8 -*-


#
# Given a collection of distinct numbers, return all possible permutations.
#
#
#
# For example,
# [1,2,3] have the following permutations:
#
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]
#


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        perms = [[]]
        
        for n in nums:
            new_perms = []
            for p in perms:
                for i in range(len(p) + 1):
                    new_perms.append(p[:i] + [n] + p[i:])
            perms = new_perms
        return perms
        
