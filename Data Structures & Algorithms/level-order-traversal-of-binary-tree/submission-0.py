# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        f=[]
        if not root:
            return f
        
        q=[]
        q.append(root)

        while q:
            n = len(q)
            f.append([])
            for _ in range(n):
                cur=q.pop(0)
                f[-1].append(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
        return f