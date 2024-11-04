class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        
        # Helper function to rob a linear arrangement of houses
        def rob_linear(houses):
            prev1, prev2 = 0, 0
            for money in houses:
                temp = max(prev1, money + prev2)
                prev2 = prev1
                prev1 = temp
            return prev1
        
        # Rob excluding the last house, and rob excluding the first house
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))