# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
搜索二叉树的深度,左右子树进行递归返回左右子树的最大深度
"""


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return 0 if root is None else max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
