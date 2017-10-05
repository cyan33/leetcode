# -*- coding:utf-8 -*-


#
# Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.
#
#
# Example 1:
#
# Given tree s:
#
#      3
#     / \
#    4   5
#   / \
#  1   2
#
# Given tree t:
#
#    4 
#   / \
#  1   2
#
# Return true, because t has the same structure and node values with a subtree of s.
#
#
# Example 2:
#
# Given tree s:
#
#      3
#     / \
#    4   5
#   / \
#  1   2
#     /
#    0
#
# Given tree t:
#
#    4
#   / \
#  1   2
#
# Return false.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Trap: Greedy Search

class Solution(object):
    def isSame(self, s, t):
        if not s and not t: return True
        if not s or not t: return False
        if s.val != t.val: return False
        
        return self.isSame(s.left, t.left) and self.isSame(s.right, t.right)
        
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not s:
            return False
        bfs = [s]
        for n in bfs:
            if n.val == t.val and self.isSame(n, t):
                return True
            if n.left: bfs.append(n.left)
            if n.right: bfs.append(n.right)
        return False
            
        
        
