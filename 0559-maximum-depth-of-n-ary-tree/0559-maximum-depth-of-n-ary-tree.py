"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        queue = deque()
        queue.append(root)
        count = 0
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                if node.children:
                    for nodes in node.children:
                        queue.append(nodes)
            count += 1
        return count
        