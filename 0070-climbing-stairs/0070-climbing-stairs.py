class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Base cases
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        # Initialize variables for previous two steps
        first, second = 1, 2
        
        # Calculate number of ways for each step from 3 to n
        for i in range(3, n + 1):
            current = first + second
            first = second
            second = current
        
        return second
