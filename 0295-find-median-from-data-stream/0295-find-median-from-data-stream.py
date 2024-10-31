

class MedianFinder:

    def __init__(self):
        # Max-heap for the lower half
        self.small = []  # Inverted values to simulate max-heap
        # Min-heap for the upper half
        self.large = []

    def addNum(self, num):
        # First, add to max-heap (small) and balance
        heapq.heappush(self.small, -num)
        
        # Move the largest element of 'small' to 'large' to balance heaps
        if self.small and self.large and (-self.small[0] > self.large[0]):
            heapq.heappush(self.large, -heapq.heappop(self.small))
        
        # Ensure size property: `small` should have max 1 extra element
        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        elif len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self):
        # If `small` has one more element, return the root of `small`
        if len(self.small) > len(self.large):
            return -self.small[0]
        # If both heaps are the same size, return the average of the roots
        return (-self.small[0] + self.large[0]) / 2.0
