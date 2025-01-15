class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # Initialize the result array with zeros
        ans = [0] * (n + 1)
        
        # Fill the result array using the dynamic programming approach
        for i in range(1, n + 1):
            ans[i] = ans[i >> 1] + (i & 1)
        
        return ans