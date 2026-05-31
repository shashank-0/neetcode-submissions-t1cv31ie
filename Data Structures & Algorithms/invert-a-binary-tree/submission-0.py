# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def rec(cur):
            if cur:
                temp=cur.left
                cur.left=cur.right
                cur.right=temp
                if cur.left:
                    rec(cur.left)
                if cur.right:
                    rec(cur.right)
            else:
                return
        rec(root)
        return root