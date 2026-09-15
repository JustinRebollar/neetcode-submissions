# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        cnt = [k]
        res = [root.val]

        def dfs(node):
            if not node:
                return

            dfs(node.left)
            if cnt[0] == 0:
                return
            cnt[0] -= 1
            if cnt[0] == 0:
                res[0] = node.val
                return
            dfs(node.right)

        dfs(root)
        return res[0]