class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def backtrack(current, open_count, close_count):
            # If the current string is a valid combination
            if len(current) == 2 * n:
                result.append(current)
                return
            
            # Add an open parenthesis if possible
            if open_count < n:
                backtrack(current + "(", open_count + 1, close_count)
            
            # Add a close parenthesis if possible
            if close_count < open_count:
                backtrack(current + ")", open_count, close_count + 1)
        
        result = []
        backtrack("", 0, 0)
        return result