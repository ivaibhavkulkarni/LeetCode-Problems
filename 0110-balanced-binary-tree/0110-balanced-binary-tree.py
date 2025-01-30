# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def checkHeight(node):
            if not node:
                return 0  # Height of an empty tree is 0
            
            left_height = checkHeight(node.left)
            if left_height == -1:
                return -1  # Left subtree is unbalanced
            
            right_height = checkHeight(node.right)
            if right_height == -1:
                return -1  # Right subtree is unbalanced
            
            if abs(left_height - right_height) > 1:
                return -1  # Current tree is unbalanced
            
            return max(left_height, right_height) + 1  # Return height of subtree
        
        return checkHeight(root) != -1