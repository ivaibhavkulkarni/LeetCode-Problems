class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        seen = set()
        for i in range(len(nums)):
            num = nums[i]

            if num in seen:
                return True
            
            else:
                seen.add(num)

            if i >= k:
                seen.remove(nums[i-k])

        return False