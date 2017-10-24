# -*- coding:utf-8 -*-


# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2.
#
# Note:
#
# The length of both num1 and num2 is < 110.
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.
#


from functools import reduce

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        indices = [0] * (len(num1) + len(num2))
        
        num1, num2 = ''.join(list(reversed(num1))), ''.join(list(reversed(num2)))
        
        for j in range(len(num2)):
            for i in range(len(num1)):
                res = int(num1[i]) * int(num2[j])
                indices[i + j + 1] += res // 10
                indices[i + j] += res % 10
                
        for k in range(len(indices)):
            if indices[k] >= 10:
                carry = indices[k] // 10
                indices[k] %= 10
                indices[k + 1] += carry
            
        res = reduce(lambda accu, curr: accu + str(curr), list(reversed(indices)), '')
        return res.lstrip('0') if res.lstrip('0') else '0'
                    
