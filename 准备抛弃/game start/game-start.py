#这个程序的目标是启动！游戏时让玩家选择启动方式，然后加载游戏。
import tkinter as tk
import subprocess
from tkinter import font
#变量们
root = tk.Tk()
C=10
D=1
F=200
E= F-(C*10+0)
G = '华康翩翩体W5-A'
H = '宋体'
I = H
s = font.families()
#检查用户是否有华康翩翩体W5-A字体
if G in s:
    I = G
root.title("游戏启动器的启动器")
# 设置窗口大小
root.geometry("400x300")
root.resizable(False, False)
# 创建一个函数
def B():
    subprocess.Popen(["others-airport-start.exe"]) 
    root.quit()
# 创建一个函数
def A():
    subprocess.Popen(["RJOO-start.exe"]) 
    root.quit()
# 创建一个标签
label = tk.Label(root, text="选择你的机场！", font=(I, 24),width=20, height=2)
label.pack(pady=20)
# 创建一个按钮
button = tk.Button(root, text="其他的", font=(I, 14),command=B,width=C, height=D)
button.place(x=F, y=F)
#创建另一个按钮
button = tk.Button(root, text="RJOO", font=(I, 14),command=A,width=C, height=D)
button.place(x=E, y=F)
# 运行主循环
root.mainloop()