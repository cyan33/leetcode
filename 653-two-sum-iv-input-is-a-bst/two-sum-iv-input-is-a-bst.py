# -*- coding:utf-8 -*-


# Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.
#
# Example 1:
#
# Input: 
#     5
#    / \
#   3   6
#  / \   \
# 2   4   7
#
# Target = 9
#
# Output: True
#
#
#
#
# Example 2:
#
# Input: 
#     5
#    / \
#   3   6
#  / \   \
# 2   4   7
#
# Target = 28
#
# Output: False
#
#
#


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if not root:
            return False
        bfs, s = [root], set()
        for i in bfs:
            if k - i.val in s:
                return True
            
            s.add(i.val)
            
            if i.left:
                bfs.append(i.left)
            if i.right:
                bfs.append(i.right)
        return False
