class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]
        
        # Initialize two variables to store maximum amounts up to two previous houses
        prev1 = 0  # max money up to house i-1
        prev2 = 0  # max money up to house i-2
        
        for num in nums:
            # Calculate the max money if robbing the current house
            temp = max(prev1, num + prev2)
            # Update prev2 and prev1 for the next house
            prev2 = prev1
            prev1 = temp
        
        # prev1 will contain the maximum amount we can rob
        return prev1