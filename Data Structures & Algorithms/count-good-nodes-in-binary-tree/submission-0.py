# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.cntNodes(root,root.val)
        
        
    def cntNodes(self,root,mx):
        if not root:
            return 0
        
        if root.val>=mx:
            return 1 + self.cntNodes(root.left,root.val) + self.cntNodes(root.right,root.val)
        else:
            return self.cntNodes(root.left,mx) + self.cntNodes(root.right,mx)