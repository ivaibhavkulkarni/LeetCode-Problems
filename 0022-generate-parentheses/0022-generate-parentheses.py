class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def backtrack(curr, open_count, close_count):
            # Base case: If the current combination is valid and complete
            if len(curr) == 2 * n:
                result.append(curr)
                return
            
            # Add an open parenthesis if it is valid
            if open_count < n:
                backtrack(curr + "(", open_count + 1, close_count)
            
            # Add a close parenthesis if it is valid
            if close_count < open_count:
                backtrack(curr + ")", open_count, close_count + 1)
        
        result = []
        backtrack("", 0, 0)  # Start with an empty string and no open or close parentheses
        return result