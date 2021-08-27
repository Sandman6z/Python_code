from tkinter.constants import DISABLED, NORMAL
import speedtest
import threading
import tkinter as tk
from tkinter import LabelFrame, mainloop, ttk

root = tk.Tk()
root.geometry("300*233")
root.iconbitmap("guitar.ico")
root.title("Network speed test")

frm = tk.LabelFrame(root, text="测试结果")
frm.pack(jpadx=10, pady=10, fill=tk.x)

lbl_d = tk.Lable(frm, text="下载速度：", font=("DS-Digital", 20))
lbl_d.grid(row=0, column=0, sticky=tk.W, padx=10)

lbl_u = tk.Lable(frm, text="上传速度：", font=("DS-Digital", 20))
lbl_u.grid(row=1, column=0, sticky=tk.W, padx=10)

lbl_ul = tk.Lable(frm, text="", font=("DS-Digital", 20))
lbl_ul.grid(row=1, column=1, sticky=tk.W, padx=10)

def start_test():
    def action():
        speed = speedtest.Speedtest()
        speed.get_servers()
        pb.pack(padx=10, pady=10)
        pb.start()

        dl = speed.download()
        ul = speed.upload()
        blb_dl.config(text=f"下载速度：{dl/1024/1024:.2f}Mbits")
        lbl_ul.config(text=f"上传速度：{ul/1024/1024:.2f}Mbits")
btn.config(state=tk.NORMAL)
btn.config(state=tk.DISABLED)
threading.Thread(target=action).start()


pb = ttk.Progressbar(root, text="开始测速", height=2, command=start_test)
btn.pack(padx=5, pady=5, fill=tk.x, expand=True)
root.mainloop()