class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.diameter = 0
        
        def depth(node):
            if not node:
                return 0
            
            left_depth = depth(node.left)
            right_depth = depth(node.right)
            
            # Update the diameter at this node
            self.diameter = max(self.diameter, left_depth + right_depth)
            
            # Return the height of the current node
            return max(left_depth, right_depth) + 1
        
        depth(root)
        return self.diameter
