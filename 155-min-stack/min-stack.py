# -*- coding:utf-8 -*-


#
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
#
#
# push(x) -- Push element x onto stack.
#
#
# pop() -- Removes the element on top of the stack.
#
#
# top() -- Get the top element.
#
#
# getMin() -- Retrieve the minimum element in the stack.
#
#
#
#
# Example:
#
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> Returns -3.
# minStack.pop();
# minStack.top();      --> Returns 0.
# minStack.getMin();   --> Returns -2.
#


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        # for each element in data, it's [value, currMin]
        self.data = []
        
    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        prevMin = self.getMin()
        if x < prevMin or prevMin == None:
            self.data.append([x, x])
        else:
            self.data.append([x, prevMin])

    def pop(self):
        """
        :rtype: void
        """
        if len(self.data) == 0:
            return None
        self.data.pop()
        
    def top(self):
        """
        :rtype: int
        """
        if len(self.data) == 0:
            return None
        return self.data[-1][0]
        

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.data) == 0:
            return None
        return self.data[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
