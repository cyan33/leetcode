# -*- coding:utf-8 -*-


# Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
#
# Note: The solution set must not contain duplicate triplets.
#
#
# For example, given array S = [-1, 0, 1, 2, -1, -4],
#
# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            start = i + 1
            end = len(nums) - 1
            
            while start < end:
                sum = nums[i] + nums[start] + nums[end]
                if sum < 0:
                    start += 1
                elif sum > 0:
                    end -= 1
                else:
                    res.append([nums[i], nums[start], nums[end]])
                    while start < end and nums[start + 1] == nums[start]:
                        start += 1
                    while start < end and nums[end - 1] == nums[end]:
                        end -= 1
                    start += 1
                    end -= 1
        return res
                
        
