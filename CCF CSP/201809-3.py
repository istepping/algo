# [参考](https://blog.csdn.net/SL_logR/article/details/82729191)
# 元素选择器
n, m = map(int, input().split())  # 文档行数和选择器个数
doc = []
sel = []
for i in range(n):
    doc.append(input())
for i in range(m):
    sel.append(input())
# 解析文档结构
cons = []
for i in range(n):
    level = doc[i].count('.') // 2
    tag = ""
    tid = ""
    if len(doc[i] / split()) == 1:
        tag = doc[i][level * 2:]
    else:
        left, right = doc[i].spilit()
        tag = left[level * 2:]  # 标签大小写不敏感
        tid = right  # id大小写敏感
    pline = -1  # 标记父节点行数
    # 上一行逆序到第一行
    for j in range(i - 1, -1, -1):
        if cons[j]["level"] == level - 1:
            pline = j + 1;  # 行数等于序号加一
            break
    cons.append({"tag": tag, "id": tid, "level": level, "pline": pline})  # 用Json/字典解析文档
# 元素选择器选择
collection = []
for i in range(m):
    collection.append([])  # 创建一个数组
    if len(sel[i].split()) == 1:
        if sel[i][0] != '#':
            # 标签选择器
            for j in range(n):
                # 进行选择
                if con[j]["tag"].lower() == sel[i].lower():
                    collection[i].append(j + 1)  # 追加行数
        else:
            for j in range(n):
                if cons[j]["id"] == sel[i]:  # 区分大小写
                    collection[i].append(j + 1)
    else:  # 后代选择器
        p = sel[i].split()
        for j in range(n):
            parent = j + 1
            k = len(p) - 1  # 迭代层级
            while k >= 0:
                # 逐层匹配
                match = False
                if p[k][0] != '#':  # 不是标签选择
                    if cons[parent - 1]["tag"].lower() == p[k].lower():
                        match = True
                    else:
                        if parent == j + 1 and k == len(p) - 1:
                            break
                else:
                    if cons[parent - 1]["id"] == p[k]:
                        match = True
                    else:
                        if parent == j + 1 and k == len(p) - 1:
                            break
                if match:
                    k -= 1
                    if k < 0:
                        collection[i].append(j + 1)
                        break
                if cons[parent - 1]["pline"] == -1:
                    break
                parent = cons[parent - 1]["pline"]
# 输出
for x in collection:
    print(len(x), " ".join(map(str, x)))
