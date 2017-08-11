# -- coding: utf-8 --

class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        (value, min_value)
        """
        self.q = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if self.getMin() is None:
            next_min = x
        else:
            next_min = min(self.getMin(), x)
        self.q.append((x, next_min))


    def pop(self):
        """
        :rtype: void
        """
        self.q.pop()

    def top(self):
        """
        :rtype: int
        """
        if not self.q:
            return None
        return self.q[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        if not self.q:
            return None
        return self.q[-1][1]




        # Your MinStack object will be instantiated and called as such:
        # obj = MinStack()
        # obj.push(x)
        # obj.pop()
        # param_3 = obj.top()
        # param_4 = obj.getMin()