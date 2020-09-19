"""
二叉树的遍历(深度优先搜索DFS):前序，中序，后序。都有递归和非递归实现方式。
前序: 先访问根节点，然后左子树，然后右子树。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 前序递归
def preorderRe(root):
    # 退出递归
    if root is None:
        return
    # 先访问
    print(root.val)
    preorderRe(root.left)
    preorderRe(root.right)


# 前序非递归: 右子树入栈->左子树入栈->弹栈重复操作 代码:建栈,栈空为条件,访问根节点,右子树入栈,左子树入栈,弹栈
def preorderNoRe(root):
    stack = [root]
    while len(stack) > 0:
        print(root.val)
        if root.right is not None:
            stack.append(root.right)
        if root.left is not None:
            stack.append(root.left)
        root = stack.pop(-1)
