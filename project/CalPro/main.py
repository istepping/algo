import tkinter as tk
from event import *

# 窗口设置
window = tk.Tk()
window.title("计算加权值")
window.geometry("500x400")

# 输入区域

lab1 = tk.Label(window, text='e1', font=('Arial', 12), width=5, height=2)
input1 = tk.Entry(window, show=None, font=('Arial', 12), width=13)
lab2 = tk.Label(window, text='e2', font=('Arial', 12), width=5, height=2)
input2 = tk.Entry(window, show=None, font=('Arial', 12), width=13)

a_lab1 = tk.Label(window, text='a1', font=('Arial', 12), width=5, height=2)
a_input1 = tk.Label(window, bg="white", font=('Arial', 12), width=13)
a_lab2 = tk.Label(window, text='a2', font=('Arial', 12), width=5, height=2)
a_input2 = tk.Label(window, bg="white", font=('Arial', 12), width=13)
p_lab1 = tk.Label(window, text='p1', font=('Arial', 12), width=5, height=2)
p_input1 = tk.Label(window, bg="white", font=('Arial', 12), width=13)
p_lab2 = tk.Label(window, text='p2', font=('Arial', 12), width=5, height=2)
p_input2 = tk.Label(window, bg="white", font=('Arial', 12), width=13)
# 输出区域

l_result = tk.Label(window, text='显示结果', bg="white", font=('Arial', 12), width=28, height=2)
b_calc = tk.Button(window, text='计算', font=('Arial', 12), width=10, height=1,
                   command=lambda: calc(lab=l_result, in1=input1.get(), in2=input2.get(), a_input1=a_input1,
                                        a_input2=a_input2, p_input1=p_input1, p_input2=p_input2))

# 布局设置
lab1.place(x=30, y=10, anchor="nw")
input1.place(x=70, y=20, anchor="nw")
lab2.place(x=200, y=10, anchor="nw")
input2.place(x=240, y=20, anchor="nw")

a_lab1.place(x=30, y=60, anchor="nw")
a_input1.place(x=70, y=70, anchor="nw")
a_lab2.place(x=200, y=60, anchor="nw")
a_input2.place(x=240, y=70, anchor="nw")

p_lab1.place(x=30, y=110, anchor="nw")
p_input1.place(x=70, y=120, anchor="nw")
p_lab2.place(x=200, y=110, anchor="nw")
p_input2.place(x=240, y=120, anchor="nw")

b_calc.place(x=350, y=180, anchor="nw")
l_result.place(x=50, y=178, anchor="nw")
# 显示窗口
window.mainloop()
