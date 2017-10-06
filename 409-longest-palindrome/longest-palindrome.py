# -*- coding:utf-8 -*-


# Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.
#
# This is case sensitive, for example "Aa" is not considered a palindrome here.
#
# Note:
# Assume the length of given string will not exceed 1,010.
#
#
# Example: 
#
# Input:
# "abccccdd"
#
# Output:
# 7
#
# Explanation:
# One longest palindrome that can be built is "dccaccd", whose length is 7.
#


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        # use a hash to store which letter has been recorded
        dic = {}
        count = 0
        hasOdd = False
        
        for c in s:
            if c in dic:
                continue
            dic[c] = True
            freq = s.count(c)
            if freq % 2 == 1:
                hasOdd = True
                count += freq - 1
            else:
                count += freq
        return count + 1 if hasOdd else count
        
