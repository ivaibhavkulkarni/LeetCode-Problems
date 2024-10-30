class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        t_count = Counter(t)
        window_count = {}
        
        left = 0
        min_len = float('inf')
        min_start = 0
        match_count = 0 
        
        for right in range(len(s)):
            char = s[right]
            window_count[char] = window_count.get(char, 0) + 1
            
            if char in t_count and window_count[char] == t_count[char]:
                match_count += 1
            
            while match_count == len(t_count):
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_start = left
                
                left_char = s[left]
                window_count[left_char] -= 1
                if left_char in t_count and window_count[left_char] < t_count[left_char]:
                    match_count -= 1
                
                left += 1
        
        return s[min_start:min_start + min_len] if min_len != float('inf') else ""
        