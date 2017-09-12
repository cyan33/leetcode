# -*- coding:utf-8 -*-


# Given a non-empty integer array of size n, find the minimum number of moves required to make all array elements equal, where a move is incrementing n - 1 elements by 1.
#
# Example:
#
# Input:
# [1,2,3]
#
# Output:
# 3
#
# Explanation:
# Only three moves are needed (remember each move increments two elements):
#
# [1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]
#


class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
#         if len(nums) == 1:
#             return 0
        
#         max_idx_count = len([i for i, val in enumerate(nums) if val == max(nums)])
#         if max_idx_count == 1 and max(nums) - min(nums) == 1:
#             return 1
#         else:
#             # do the increment for the n - 1 elements
#             max_val = max(nums)
#             nums.remove(max_val)    # remove only one max value, not all the duplicated
#             next_nums = [n + 1 for n in nums]
#             next_nums.append(max_val)        
#             return 1 + self.minMoves(next_nums)
            
        # This is a fucking MATH problem
        return sum(nums) - min(nums) * len(nums)

