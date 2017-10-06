# -*- coding:utf-8 -*-


#
# Given a string, your task is to count how many palindromic substrings in this string.
#
#
#
# The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters. 
#
#
# Example 1:
#
# Input: "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".
#
#
#
# Example 2:
#
# Input: "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
#
#
#
# Note:
#
# The input string length won't exceed 1000.
#


class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        for center in range(len(s) * 2 - 1):
            left = center // 2
            right = left + center % 2
            while left >= 0 and right <= len(s) - 1 and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
        return count
        
