class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return ""
        
        start, end = 0, 0

        def expandAroundCenter(left, right):
            # Expand as long as we have a palindrome
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Return the bounds of the palindrome
            return left + 1, right - 1

        for i in range(len(s)):
            # Odd length palindromes
            left1, right1 = expandAroundCenter(i, i)
            # Even length palindromes
            left2, right2 = expandAroundCenter(i, i + 1)

            # Update the longest palindrome if needed
            if right1 - left1 > end - start:
                start, end = left1, right1
            if right2 - left2 > end - start:
                start, end = left2, right2

        return s[start:end + 1]