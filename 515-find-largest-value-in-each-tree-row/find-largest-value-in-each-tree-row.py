# -*- coding:utf-8 -*-


# You need to find the largest value in each row of a binary tree.
#
# Example:
#
# Input: 
#
#           1
#          / \
#         3   2
#        / \   \  
#       5   3   9 
#
# Output: [1, 3, 9]
#
#


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from functools import reduce
class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        maxes = []
        row = [root]
        while any(row):
            maxes.append(max([n.val for n in row]))
            row = [kid for n in row for kid in [n.left, n.right] if kid]
        return maxes
