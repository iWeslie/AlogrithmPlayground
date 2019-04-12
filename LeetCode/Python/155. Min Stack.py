class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.list = []
        self.min = float('inf')

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.list.append(x)

    def pop(self):
        """
        :rtype: None
        """
        self.list.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.list[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return min(self.list)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
