class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Step 1: Count the frequency of each element
        freq_map = {}
        for num in nums:
            if num in freq_map:
                freq_map[num] += 1
            else:
                freq_map[num] = 1
        
        # Step 2: Create a list of buckets
        bucket = [[] for _ in range(len(nums) + 1)]
        
        # Step 3: Fill the bucket with elements grouped by their frequency
        for num, freq in freq_map.items():
            bucket[freq].append(num)
        
        # Step 4: Collect the top k frequent elements
        result = []
        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result