# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        if not preorder or not inorder:
            return None
        
        
        inorder_index_map = {value: index for index, value in enumerate(inorder)}

        def buildTreeRecursive(pre_start, pre_end, in_start, in_end):
            if pre_start > pre_end or in_start > in_end:
                return None
            
            root_val = preorder[pre_start]
            root = TreeNode(root_val)
            
            root_index = inorder_index_map[root_val]
            
            left_size = root_index - in_start
            
            root.left = buildTreeRecursive(pre_start + 1, pre_start + left_size, in_start, root_index - 1)
            root.right = buildTreeRecursive(pre_start + left_size + 1, pre_end, root_index + 1, in_end)
            
            return root

        return buildTreeRecursive(0, len(preorder) - 1, 0, len(inorder) - 1)