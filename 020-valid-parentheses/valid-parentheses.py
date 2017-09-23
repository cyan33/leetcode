# -*- coding:utf-8 -*-


# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 != 0:
            return False
        dict = {'}': '{', ')': '(', ']': '['}
        stack = []
        
        for p in s:
            if p in ['(', '{', '[']:
                stack.append(p)
            else:
                if len(stack) == 0 or stack.pop() != dict[p]:
                    return False
        return len(stack) == 0
    
