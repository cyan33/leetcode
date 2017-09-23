# -*- coding:utf-8 -*-


# Implement pow(x, n).


class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # if not n:
        #     return 1
        # if n == 1:
        #     return x
        # if n < 0:
        #     return 1 / self.myPow(x, -n)
        # if n % 2 != 0:
        #     return x * self.myPow(x, n - 1)
        # else:
        #     return self.myPow(x * 2, n // 2)
        
        
        if not n:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n % 2:
            return x * self.myPow(x, n-1)
        return self.myPow(x*x, n/2)
    
