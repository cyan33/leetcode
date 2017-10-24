# -*- coding:utf-8 -*-


#
# Given two binary strings, return their sum (also a binary string).
#
#
#
# For example,
# a = "11"
# b = "1"
# Return "100".


class Solution(object):
    def helper(self, a, b):
        if not b:
            return str(bin(a))[2:]
        else:
            return self.helper(a ^ b, (a & b) << 1)
    
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = int(a, 2)
        b = int(b, 2)
        
        return self.helper(a, b)
        
