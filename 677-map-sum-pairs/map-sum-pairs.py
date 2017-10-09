# -*- coding:utf-8 -*-


#
# Implement a MapSum class with insert, and sum methods.
#
#
#
# For the method insert, you'll be given a pair of (string, integer). The string represents the key and the integer represents the value. If the key already existed, then the original key-value pair will be overridden to the new one.
#
#
#
# For the method sum, you'll be given a string representing the prefix, and you need to return the sum of all the pairs' value whose key starts with the prefix.
#
#
# Example 1:
#
# Input: insert("apple", 3), Output: Null
# Input: sum("ap"), Output: 3
# Input: insert("app", 2), Output: Null
# Input: sum("ap"), Output: 5
#


class TrieNode():
    def __init__(self, count = 0):
        self.count = count
        self.children = {}
                
class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = {}

    def insert(self, key, val):
        self.map[key] = val

    def sum(self, prefix):
        return sum([val for k, val in self.map.items() if k.startswith(prefix)])        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
