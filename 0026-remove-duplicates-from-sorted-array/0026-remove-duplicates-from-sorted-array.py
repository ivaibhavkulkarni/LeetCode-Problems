class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0  # Edge case: empty list

        j = 0  # Slow pointer for unique elements
        for i in range(1, len(nums)):
            if nums[i] != nums[j]:  # Found a new unique element
                j += 1
                nums[j] = nums[i]  # Move unique element forward
        
        return j + 1  # Length of unique elements