# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        def searchTree(node):
            if node is None:
                return 0
            lDepth = searchTree(node.left)
            rDepth = searchTree(node.right)
            self.diameter = max(lDepth + rDepth, self.diameter)
            return max(lDepth, rDepth) + 1
        searchTree(root)
        return self.diameter

        