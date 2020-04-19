"""
操作给定的二叉树，将其变换为源二叉树的镜像。
"""


# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def change(self, p):
        if p is not None:
            p.left, p.right = p.right, p.left
            self.change(p.left)
            self.change(p.right)

    # 返回镜像树的根节点
    def Mirror(self, root):
        p = root
        self.change(p)
        return root
