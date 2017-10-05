# -*- coding:utf-8 -*-


# Given a linked list, remove the nth node from the end of list and return its head.
#
#
# For example,
#
#
#    Given linked list: 1->2->3->4->5, and n = 2.
#
#    After removing the second node from the end, the linked list becomes 1->2->3->5.
#
#
#
# Note:
# Given n will always be valid.
# Try to do this in one pass.


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        length = 0
        cursor = head
        
        # calculate the length of the linked list
        while cursor:
            length += 1
            cursor = cursor.next
        
        # n crosses the left boundary
        if n > length:
            return head
            
        count = length - n
        curr = head
        prev = None
        
        # if the deleted node is the head
        if count == 0:
            head = head.next
            return head
        
        # move to that node
        while count:
            prev = curr
            curr = curr.next
            count -= 1
            
        # delete that node
        prev.next = curr.next
        
        # return head
        return head
        
        
