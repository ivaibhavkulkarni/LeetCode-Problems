class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        result = 0
        for i in range(32):  # Process all 32 bits
            result <<= 1         # Shift result left by 1 to make space for the next bit
            result |= (n & 1)    # Extract the last bit of n and add it to result
            n >>= 1              # Shift n right by 1 to process the next bit
        return result
