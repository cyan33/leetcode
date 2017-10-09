# -*- coding:utf-8 -*-


# Given a collection of intervals, merge all overlapping intervals.
#
#
# For example,
# Given [1,3],[2,6],[8,10],[15,18],
# return [1,6],[8,10],[15,18].


# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals.sort(key = lambda i: i.start)
        res = []
        for i in intervals:
            if res and i.start <= res[-1].end:
                res[-1].end = max(res[-1].end, i.end)
            else:
                res.append(i)
        return res
        
