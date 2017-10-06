# -*- coding:utf-8 -*-


# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
#
# Example:
#
# Input: "babad"
#
# Output: "bab"
#
# Note: "aba" is also a valid answer.
#
#
#
# Example:
#
# Input: "cbbd"
#
# Output: "bb"
#


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = ''
        
        for center in range(2 * len(s) - 1):
            left = center // 2
            right = left + center % 2
            
            while left >= 0 and right <= len(s) - 1 and s[left] == s[right]:
                if right - left + 1 > len(ans):
                    ans = s[left:right + 1]
                left -= 1
                right += 1
        return ans
        
