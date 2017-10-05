# -*- coding:utf-8 -*-


#
# Given a binary tree, find the leftmost value in the last row of the tree. 
#
#
# Example 1:
#
# Input:
#
#     2
#    / \
#   1   3
#
# Output:
# 1
#
#
#
#   Example 2: 
#
# Input:
#
#         1
#        / \
#       2   3
#      /   / \
#     4   5   6
#        /
#       7
#
# Output:
# 7
#
#
#
# Note:
# You may assume the tree (i.e., the given root node) is not NULL.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        queue = [root]
        for node in queue:
            queue += filter(None, [node.right, node.left])
        return node.val
    
