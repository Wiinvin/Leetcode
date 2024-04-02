# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        left_val = self.inorderTraversal(root.left)
        if root.left == None and root.right == None:
            return [root.val]
        inorder_seq = [root.val]
        right_val = self.inorderTraversal(root.right)

        return left_val + inorder_seq + right_val
