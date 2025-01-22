class MinStack(object):

    def __init__(self):
        # Initialize both stacks
        self.stack = []        # Main stack to store values
        self.min_stack = []    # Stack to store the minimum values

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        # Push the value onto the main stack
        self.stack.append(val)
        
        # If the min_stack is empty or the new value is smaller or equal to the current minimum, push it to min_stack
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        """
        :rtype: None
        """
        # Pop the top element from the main stack
        val = self.stack.pop()
        
        # If the popped value is the same as the top of the min_stack, pop it from min_stack as well
        if val == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self):
        """
        :rtype: int
        """
        # Return the top element from the main stack
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        # The top element of the min_stack is the minimum element
        return self.min_stack[-1]