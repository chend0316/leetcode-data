from typing import List
from .leetcode import TreeNode

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not inorder: return None
        val = preorder.pop(0)
        index = inorder.index(val)

        root = TreeNode(val)
        root.left = self.buildTree(preorder, inorder[:index])
        root.right = self.buildTree(preorder, inorder[index + 1:])

        return root
