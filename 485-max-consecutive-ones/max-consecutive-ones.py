# -*- coding:utf-8 -*-


# Given a binary array, find the maximum number of consecutive 1s in this array.
#
# Example 1:
#
# Input: [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s.
#     The maximum number of consecutive 1s is 3.
#
#
#
# Note:
#
# The input array will only contain 0 and 1.
# The length of input array is a positive integer and will not exceed 10,000
#


class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # consecutives = [0]
        # curr = 0
        # for idx, num in enumerate(nums):
            # if num == 0:
                # consecutives.append(curr)
                # curr = 0
            # elif num == 1 and idx == len(nums) - 1:
                # curr += 1
                # consecutives.append(curr)
            # else:
                # curr += 1
                
        # return max(consecutives)
        
        res = 0
        curr = 0
        for num in nums:
            if num == 1:
                curr += 1
                res = max(curr, res)
            else:
                curr = 0
        return res
