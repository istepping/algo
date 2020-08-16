import tkinter.messagebox as tkm
import util


def update(a_input1, a_input2, p_input1, p_input2):
    print("update")


def calc(lab, in1, in2, a_input1, a_input2, p_input1, p_input2):
    print("计算")
    print(in1)
    print(in2)
    l1 = in1.split()
    l2 = in2.split()
    # 校验:概率和，向量维度
    if len(l1) != len(l2):
        tkm.showwarning(title="提示", message="e1和e2向量维度不同")
        return
    if sum(float(i) for i in l1) != 1:
        tkm.showwarning(title="提示", message="e1概率和不为1")
        return
    if sum(float(i) for i in l2) != 1:
        tkm.showwarning(title="提示", message="e2概率和不为1")
        return

    # 同步跟新
    a_input1["text"] = in1
    a_input2["text"] = in2
    p_input1["text"] = in1
    p_input2["text"] = in2
    # 计算
    result = util.calc_weight(l1, l2)
    lab["text"] = str(result)
