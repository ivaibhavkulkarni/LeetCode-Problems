class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        # Step 1: Sort the intervals based on their end times
        intervals.sort(key=lambda x: x[1])
        
        # Step 2: Initialize variables
        non_overlap_count = 0
        prev_end = float('-inf')
        
        # Step 3: Iterate through intervals
        for start, end in intervals:
            if start >= prev_end:
                # No overlap, update prev_end
                prev_end = end
                non_overlap_count += 1
            # Else, overlap exists; we skip this interval (remove it)
        
        # Step 4: Total intervals minus non-overlapping intervals gives removed intervals
        return len(intervals) - non_overlap_count