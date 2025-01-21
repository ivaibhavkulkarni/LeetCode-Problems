class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        mask = 0xFFFFFFFF  # To simulate 32-bit signed integers
        max_int = 0x7FFFFFFF  # Max positive integer in 32-bit
        
        while b != 0:
            # Calculate sum without carry
            temp = (a ^ b) & mask
            # Calculate carry
            b = ((a & b) << 1) & mask
            a = temp  # Update a to the new sum
        
        # If a is negative, convert to negative 32-bit integer
        return a if a <= max_int else ~(a ^ mask)