"""
输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSubTree(self, root1, root2):
        # 重复问题,root2是不是root1的子树,递归终点,root2先判断,root1后判断
        if root2 is None:
            return True
        if root1 is None:
            return False
        if root1.val == root2.val:
            return self.isSubTree(root1.left, root2.left) and self.isSubTree(root1.right, root2.right)
        else:
            return False

    def HasSubtree(self, pRoot1, pRoot2):
        if pRoot1 is None or pRoot2 is None:
            return False
        # 递归思路: 根节点开始, 左节点开始, 右节点开始
        return self.isSubTree(pRoot1, pRoot2) or self.isSubTree(pRoot1.left, pRoot2) or self.isSubTree(pRoot1.right,
                                                                                                       pRoot2)
