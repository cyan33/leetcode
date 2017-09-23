# -*- coding:utf-8 -*-


#
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
#
# P   A   H   N
# A P L S I I G
# Y   I   R
#
#
# And then read line by line: "PAHNAPLSIIGYIR"
#
#
# Write the code that will take a string and make this conversion given a number of rows:
#
# string convert(string text, int nRows);
#
# convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if len(s) <= numRows or numRows == 1:
            return s
        
        patternLen = numRows + numRows - 2
        res = [''] * numRows

        for i in range(len(s)):
            pos = i % patternLen
            
            if pos < numRows:
                # zig
                res[pos] += s[i]
            else:
                # zag
                res[numRows - 2 - (pos - numRows)] += s[i]
                
        return ''.join(res)
        
