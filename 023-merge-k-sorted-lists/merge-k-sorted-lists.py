# -*- coding:utf-8 -*-


#
# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        res = []
        for l in lists:
            while l:
                res.append(l.val)
                l = l.next
        return sorted(res)
        
