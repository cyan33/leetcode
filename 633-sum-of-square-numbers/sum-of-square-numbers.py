# -*- coding:utf-8 -*-


#
# Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a2 + b2 = c.
#
#
# Example 1:
#
# Input: 5
# Output: True
# Explanation: 1 * 1 + 2 * 2 = 5
#
#
#
#
# Example 2:
#
# Input: 3
# Output: False
#
#


import math
class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        left = 0
        right = int(math.sqrt(c))
        
        while left <= right:
            curr = left ** 2 + right ** 2
            if curr < c:
                left += 1
            elif curr > c:
                right -= 1
            else:
                return True
            
        return False
        
        
