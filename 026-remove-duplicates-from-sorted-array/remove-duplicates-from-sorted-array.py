# -*- coding:utf-8 -*-


#
# Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.
#
#
# Do not allocate extra space for another array, you must do this in place with constant memory.
#
#
#
# For example,
# Given input array nums = [1,1,2],
#
#
# Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # the description is misleading!
        # I don't know why I cannot use "set"
        if len(nums) == 0:
            return 0
        read = 1
        write = 1
        while read < len(nums):
            if nums[read] != nums[read - 1]:
                nums[write] = nums[read]
                write += 1
            read += 1
        return write
    
