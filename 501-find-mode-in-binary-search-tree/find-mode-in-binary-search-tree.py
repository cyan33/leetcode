# -*- coding:utf-8 -*-


# Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.
#
#
# Assume a BST is defined as follows:
#
# The left subtree of a node contains only nodes with keys less than or equal to the node's key.
# The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
# Both the left and right subtrees must also be binary search trees.
#
#
#
#
# For example:
# Given BST [1,null,2,2],
#
#    1
#     \
#      2
#     /
#    2
#
#
#
# return [2].
#
#
# Note:
# If a tree has more than one mode, you can return them in any order.
#
#
# Follow up:
# Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).


from collections import Counter
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.counter = Counter()
    def traverseTree(self, node):
        if node:
            self.counter[node.val] = self.counter.get(node.val, 0) + 1
            self.traverseTree(node.left)
            self.traverseTree(node.right)
            
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        
        # traverse and save each value into the counter
        self.traverseTree(root)
        # return the max elements in an array
        res = set()
        max = 0
        for k, v in self.counter.most_common():
            max = v if v > max else max
            if v < max:
                break
            res.add(k)
        return list(res)
        
        
