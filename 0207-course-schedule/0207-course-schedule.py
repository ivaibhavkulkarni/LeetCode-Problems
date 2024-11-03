class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # Build adjacency list and in-degree array
        adj_list = defaultdict(list)
        in_degree = [0] * numCourses
        
        # Populate adjacency list and in-degree array
        for dest, src in prerequisites:
            adj_list[src].append(dest)
            in_degree[dest] += 1
        
        # Initialize queue with courses having zero in-degree
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        visited_courses = 0
        
        # Process courses in topological order
        while queue:
            course = queue.popleft()
            visited_courses += 1
            for neighbor in adj_list[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # If we visited all courses, there is no cycle
        return visited_courses == numCourses