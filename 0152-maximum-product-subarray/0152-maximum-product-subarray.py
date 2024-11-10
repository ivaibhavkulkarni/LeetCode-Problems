class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_prod = min_prod = result = nums[0]
        
        # Iterate over the array from the second element
        for num in nums[1:]:
            if num < 0:
                # Swap max_prod and min_prod when encountering a negative number
                max_prod, min_prod = min_prod, max_prod
            
            # Update max_prod and min_prod
            max_prod = max(num, max_prod * num)
            min_prod = min(num, min_prod * num)
            
            # Update the result with the maximum product found so far
            result = max(result, max_prod)
        
        return result