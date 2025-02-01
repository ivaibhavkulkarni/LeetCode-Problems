class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.min_heap = []
        
        # Initialize the heap with the k largest elements
        for num in nums:
            self.add(num)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        heapq.heappush(self.min_heap, val)  # Add the new element

        if len(self.min_heap) > self.k:  # Ensure heap size is at most k
            heapq.heappop(self.min_heap)

        return self.min_heap[0]  # The root of the heap is the kth largest element