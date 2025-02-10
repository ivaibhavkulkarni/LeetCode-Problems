import heapq

class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        # Use a min-heap to store (distance, point) pairs
        heap = []
        for x, y in points:
            dist = x**2 + y**2  # Squared Euclidean distance
            heapq.heappush(heap, (dist, [x, y]))
        
        # Extract the k closest points
        result = []
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])
        
        return result
