class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Initialize the result array with zeros
        result = [0] * len(temperatures)
        # Stack to keep track of indices where we haven't found a warmer day
        stack = []

        for i, temp in enumerate(temperatures):
            # While stack is not empty and current temperature is greater
            # than the temperature at the index stored in the stack
            while stack and temperatures[stack[-1]] < temp:
                prev_index = stack.pop()
                result[prev_index] = i - prev_index
            # Push the current index onto the stack
            stack.append(i)
        
        return result
