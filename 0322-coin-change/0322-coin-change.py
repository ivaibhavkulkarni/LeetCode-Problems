class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0  # Base case: 0 coins are needed to make amount 0

        # Iterate through each coin
        for coin in coins:
            # Update the dp array for amounts from coin to amount
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)

        # Check if amount can be made up
        return dp[amount] if dp[amount] != float('inf') else -1