class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s[0] == '0':
            return 0
        
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1  # Base case: an empty string
        dp[1] = 1  # Base case: one valid decoding for a non-zero first digit

        for i in range(2, n + 1):
            # Check the last single digit
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]
            
            # Check the last two digits
            two_digit = int(s[i - 2:i])  # Convert substring to an integer
            if 10 <= two_digit <= 26:
                dp[i] += dp[i - 2]

        return dp[n]
