class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current_sum = nums[0]
        max_sum = nums[0]
        
        # Iterate through the array starting from the second element
        for i in range(1, len(nums)):
            # Update the current sum to be the maximum of adding the current element
            # or starting a new subarray from the current element
            current_sum = max(nums[i], current_sum + nums[i])
            
            # Update the maximum sum found so far
            max_sum = max(max_sum, current_sum)
        
        return max_sum