class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        num = set()

        for i in nums:
            if i in num:
                return True
            else:
                num.add(i)
            
        return False