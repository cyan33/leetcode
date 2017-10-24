# -*- coding:utf-8 -*-


#
# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
#
#
#
# For example,
# "A man, a plan, a canal: Panama" is a palindrome.
# "race a car" is not a palindrome.
#
#
#
# Note:
# Have you consider that the string might be empty? This is a good question to ask during an interview.
#
# For the purpose of this problem, we define empty string as valid palindrome.


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        allow = [chr(x) for x in range(ord('a'), ord('z') + 1)]
        allow += [str(x) for x in range(10)]
        
        # reconstruct the string
        s = filter(lambda x: x in allow, s.lower())

        left = 0
        right = len(s) - 1
        
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True
        
