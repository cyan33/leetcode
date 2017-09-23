# -*- coding:utf-8 -*-


#
# Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.


class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # doesn't have duplicates
        if len(nums) == len(set(nums)):
            return False

        # search for i and j
        for i in range(len(nums)):
            if nums.count(nums[i]) < 2:
                continue
            else:
                if not nums[i] in nums[i + 1:]:
                    continue

                j = nums[i + 1:].index(nums[i]) + i + 1

                if abs(i - j) <= k:
                    return True
        return False
                
        
