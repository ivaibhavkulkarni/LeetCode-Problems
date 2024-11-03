# Definition for a Node.
class Node(object):
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None

        # Dictionary to store the mapping from original node to its clone
        cloned_nodes = {}

        def dfs(original_node):
            # If the node is already cloned, return the clone
            if original_node in cloned_nodes:
                return cloned_nodes[original_node]

            # Create a clone for the current node
            clone = Node(original_node.val)
            cloned_nodes[original_node] = clone

            # Recursively clone all the neighbors
            for neighbor in original_node.neighbors:
                clone.neighbors.append(dfs(neighbor))

            return clone

        # Start the DFS from the given node
        return dfs(node)
