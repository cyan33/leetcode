# -*- coding:utf-8 -*-


# Write a function to find the longest common prefix string amongst an array of strings.


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
    
        strs.sort(key = lambda x: len(x))
        
        prefix = strs[0]
        # prefix could be "sch" for ['schema', 'schetuad', 'school', 'schalost']
        
        for i in range(1, len(strs)):
            while strs[i][:len(prefix)] != prefix:
                prefix = prefix[:-1]
                if prefix == '':
                    return ''
                
        return prefix
        
