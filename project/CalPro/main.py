import tkinter as tk
from event import *

# 窗口设置
window = tk.Tk()
window.title("计算加权值")
window.geometry("500x400")

# 输入区域
photo1 = tk.PhotoImage(file='e1.png')
photo2 = tk.PhotoImage(file='e2.png')
photo3 = tk.PhotoImage(file='a1.png')
photo4 = tk.PhotoImage(file='a2.png')
photo5 = tk.PhotoImage(file='p1.png')
photo6 = tk.PhotoImage(file='p2.png')
lab1 = tk.Label(window, image=photo1)
input1 = tk.Entry(window, show=None, font=('Arial', 12), width=13)
lab2 = tk.Label(window, image=photo2)
input2 = tk.Entry(window, show=None, font=('Arial', 12), width=13)

a_lab1 = tk.Label(window, image=photo3)
a_input1 = tk.Label(window, bg="white", font=('Arial', 12), width=13)
a_lab2 = tk.Label(window, image=photo4)
a_input2 = tk.Label(window, bg="white", font=('Arial', 12), width=13)
p_lab1 = tk.Label(window, image=photo5)
p_input1 = tk.Label(window, bg="white", font=('Arial', 12), width=13)
p_lab2 = tk.Label(window, image=photo6)
p_input2 = tk.Label(window, bg="white", font=('Arial', 12), width=13)
# 输出区域

l_result = tk.Label(window, text='显示结果', bg="white", font=('Arial', 12), width=28, height=2)
b_calc = tk.Button(window, text='计算', font=('Arial', 12), width=10, height=1,
                   command=lambda: calc(lab=l_result, in1=input1.get(), in2=input2.get(), a_input1=a_input1,
                                        a_input2=a_input2, p_input1=p_input1, p_input2=p_input2))

# 布局设置
lab1.place(x=45, y=18, anchor="nw")
input1.place(x=70, y=20, anchor="nw")
lab2.place(x=215, y=18, anchor="nw")
input2.place(x=240, y=20, anchor="nw")

a_lab1.place(x=45, y=68, anchor="nw")
a_input1.place(x=70, y=70, anchor="nw")
a_lab2.place(x=215, y=68, anchor="nw")
a_input2.place(x=240, y=70, anchor="nw")

p_lab1.place(x=45, y=118, anchor="nw")
p_input1.place(x=70, y=120, anchor="nw")
p_lab2.place(x=215, y=118, anchor="nw")
p_input2.place(x=240, y=120, anchor="nw")

b_calc.place(x=350, y=180, anchor="nw")
l_result.place(x=50, y=178, anchor="nw")
# 显示窗口
window.mainloop()
