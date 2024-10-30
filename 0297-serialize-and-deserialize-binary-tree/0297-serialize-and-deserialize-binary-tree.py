# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def dfs(node):
            if not node:
                return ["null"] 
            return [str(node.val)] + dfs(node.left) + dfs(node.right)
        
        return ",".join(dfs(root))

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        values = data.split(",")
        
        def build_tree():
            val = next(values_iter)  
            if val == "null":
                return None
            node = TreeNode(int(val))  # Create a new TreeNode
            node.left = build_tree()  # Build left subtree
            node.right = build_tree()  # Build right subtree
            return node
        
        values_iter = iter(values)
        return build_tree()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))