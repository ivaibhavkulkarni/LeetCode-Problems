class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_reach = 0
        
        # Iterate through the array
        for i in range(len(nums)):
            # If the current index is beyond the maximum reachable index, return False
            if i > max_reach:
                return False
            
            # Update the maximum reachable index
            max_reach = max(max_reach, i + nums[i])
            
            # If the maximum reachable index is greater than or equal to the last index, return True
            if max_reach >= len(nums) - 1:
                return True
        
        return False