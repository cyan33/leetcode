# -*- coding:utf-8 -*-


# Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
#
# Example 1:
#
# Input:
#     3
#    / \
#   9  20
#     /  \
#    15   7
# Output: [3, 14.5, 11]
# Explanation:
# The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
#
#
#
# Note:
#
# The range of node's value is in the range of 32-bit signed integer.
#


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if not root:
            return []
        aver = []
        bfs = [root]
        while len(bfs):
            currLvlSize = len(bfs)
            sum = float(0)
            for i in range(currLvlSize):
                sum += bfs[i].val
                if bfs[i].left: bfs.append(bfs[i].left)
                if bfs[i].right: bfs.append(bfs[i].right)
                
            for i in range(currLvlSize):
                bfs.pop(0)
                
            aver.append(sum / currLvlSize)
        
        return aver
        
