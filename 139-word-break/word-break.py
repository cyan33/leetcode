# -*- coding:utf-8 -*-


#
# Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words. You may assume the dictionary does not contain duplicate words.
#
#
# For example, given
# s = "leetcode",
# dict = ["leet", "code"].
#
#
#
# Return true because "leetcode" can be segmented as "leet code".
#
#
#
# UPDATE (2017/1/4):
# The wordDict parameter had been changed to a list of strings (instead of a set of strings). Please reload the code definition to get the latest changes.


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        
        # if s in wordDict:
        #     return True
        # else:
        #     for i in range(len(s)):
        #         if s[:i] in wordDict:
        #             return self.wordBreak(s[i:], wordDict)
        # return False
        
        d = [False] * len(s)
        
        for i in range(len(s)):
            for w in wordDict:
                if s[i-len(w)+1:i+1] == w and (d[i-len(w)] or i-len(w) < 0):
                    d[i] = True
        
        return d[-1]
