from .leetcode import TreeNode

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0
        if not root.left and not root.right: return 1
        
        if root.left and root.right:
            min_of_child = min(self.minDepth(root.left), self.minDepth(root.right))
        elif root.right:
            min_of_child = self.minDepth(root.right)
        else:
            min_of_child = self.minDepth(root.left)

        return min_of_child + 1
