"""
二叉树的遍历(深度优先搜索DFS):前序，中序，后序。都有递归和非递归实现方式。
前序: 先访问根节点，然后左子树，然后右子树。
[参考](https://www.cnblogs.com/icekx/p/9127569.html)
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 初始化
def init_tree():
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    e = TreeNode(5)
    f = TreeNode(6)
    a.left = b
    a.right = e
    b.left = c
    b.right = d
    e.right = f
    return a

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






# 中序递归
def inorderRe(root):
    if root is None:
        return
    inorderRe(root.left)
    print(root.val)
    inorderRe(root.right)


# 中序非递归:当前值入栈->走向左子树->到底后弹栈访问->转向右子树
def inorderNoRe(root):
    stack = []
    while len(stack) > 0 or root is not None:
        if root is not None:
            stack.append(root)
            root = root.left
        else:
            # 弹栈访问
            root = stack.pop()
            print(root.val)
            root = root.right


# 后序递归
def postorderRe(root):
    if root is None:
        return
    postorderRe(root.left)
    postorderRe(root.right)
    print(root.val)


# 后序非递归: 左子树,右子树顺序入栈1-> 1弹栈如栈2-> 左子树，右子树入栈1->2一次弹栈
def postorderNoRe(root):
    stack1 = [root]
    stack2 = []
    while len(stack1) > 0:
        root = stack1.pop()
        stack2.append(root)
        if root.left is not None:
            stack1.append(root.left)
        if root.right is not None:
            stack1.append(root.right)
    while len(stack2) > 0:
        print(stack2.pop().val)


# main
if __name__ == "__main__":
    node = init_tree()
    postorderNoRe(node)
    postorderRe(node)
