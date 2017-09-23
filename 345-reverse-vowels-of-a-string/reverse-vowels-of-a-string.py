# -*- coding:utf-8 -*-


# Write a function that takes a string as input and reverse only the vowels of a string.
#
#
# Example 1:
# Given s = "hello", return "holle".
#
#
#
# Example 2:
# Given s = "leetcode", return "leotcede".
#
#
#
# Note:
# The vowels does not include the letter "y".


class Solution(object):
    # 'leetcode'
    #   ^^  ^ ^
    def isVowel(self, c):
        return c in 'aeiouAEIOU'
    
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        # get all indexes of the vowels in s
        vIndexes = []
        
        for i, c in enumerate(s):
            if self.isVowel(c):
                vIndexes.append(i)
        
        left = 0
        right = len(vIndexes) - 1
        
        while left < right:
            s[vIndexes[left]], s[vIndexes[right]] = s[vIndexes[right]], s[vIndexes[left]]
            left += 1
            right -= 1
            
        return "".join(s)
            
        
