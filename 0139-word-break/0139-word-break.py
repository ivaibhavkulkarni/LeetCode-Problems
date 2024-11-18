class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        wordSet = set(wordDict)
        
        # Initialize the dp array with False
        dp = [False] * (len(s) + 1)
        
        # Base case: An empty string can be segmented
        dp[0] = True
        
        # Iterate over the string s
        for i in range(1, len(s) + 1):
            # Check all possible partitions of s[0:i]
            for j in range(i):
                # If s[j:i] is in the dictionary and dp[j] is True
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
                    break
        
        # The answer is whether the whole string can be segmented
        return dp[len(s)]