class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        def expandAroundCenter(left, right, count):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            return count

        count = 0
        for i in range(len(s)):
            count = expandAroundCenter(i, i, count)       # Count odd-length palindromes
            count = expandAroundCenter(i, i + 1, count)   # Count even-length palindromes

        return count
