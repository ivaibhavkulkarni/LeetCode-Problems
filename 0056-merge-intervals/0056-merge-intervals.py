class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=lambda x: x[0])
        
        # Initialize a list to store merged intervals
        merged = []
        
        for interval in intervals:
            # If merged is empty or the current interval does not overlap with the previous
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # Overlapping intervals, merge them
                merged[-1][1] = max(merged[-1][1], interval[1])
        
        return merged