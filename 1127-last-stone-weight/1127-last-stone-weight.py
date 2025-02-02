class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        # Convert stones list into a max heap (use negative values since Python has a min heap by default)
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        
        # Process the heap until one or zero stones remain
        while len(stones) > 1:
            # Extract the two largest stones
            first = -heapq.heappop(stones)
            second = -heapq.heappop(stones)
            
            # If they are not equal, push the difference back into the heap
            if first != second:
                heapq.heappush(stones, -(first - second))
        
        # Return the last remaining stone or 0 if none remain
        return -stones[0] if stones else 0