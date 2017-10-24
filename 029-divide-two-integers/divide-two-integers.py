# -*- coding:utf-8 -*-


#
# Divide two integers without using multiplication, division and mod operator.
#
#
# If it is overflow, return MAX_INT.


class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        positive = (dividend > 0) is (divisor > 0)
        res = 0
        
        dividend, divisor = abs(dividend), abs(divisor)
        
        while dividend >= divisor:
            temp = divisor
            i = 1
            while dividend >= (temp << 1):
                temp <<= 1
                i <<= 1
                
            dividend -= temp
            res += i
        
        res = res if positive else -res
        
        return min(max(-2147483648, res), 2147483647)
        
