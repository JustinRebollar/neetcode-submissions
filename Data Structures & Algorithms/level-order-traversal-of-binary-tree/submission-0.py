from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        queue = deque()
        queue.append(root)

        while queue:
            current_queue_len = len(queue)
            level_values = []

            for _ in range(current_queue_len):
                current_node = queue.popleft()

                if current_node:
                    level_values.append(current_node.val)

                    if current_node.left: queue.append(current_node.left)
                    if current_node.right: queue.append(current_node.right)

            if level_values: 
                res.append(level_values)
            
        return res