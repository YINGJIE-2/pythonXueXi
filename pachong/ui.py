import tkinter as tk
from tkinter import messagebox

def on_button_click():
    user_text = entry.get()
    selected_radio = radio_var.get()
    selected_checkboxes = [label for label, var in checkboxes.items() if var.get()]
    messagebox.showinfo("信息", f"你输入的是: {user_text}\n你选择了: {selected_radio}\n你选中的复选框: {', '.join(selected_checkboxes)}")

# 创建主窗口
root = tk.Tk()
root.title("简易界面")

# 创建文本输入框并放置在窗口上
entry_label = tk.Label(root, text="请输入一些文本:")
entry_label.pack(pady=5)
entry = tk.Entry(root, width=30)
entry.pack(pady=5)

# 创建单选按钮组并放置在窗口上
radio_label = tk.Label(root, text="请选择一个选项:")
radio_label.pack(pady=5)
radio_var = tk.StringVar(value="选项1")
radio_buttons = [
    tk.Radiobutton(root, text="选项1", variable=radio_var, value="选项1"),
    tk.Radiobutton(root, text="选项2", variable=radio_var, value="选项2"),
    tk.Radiobutton(root, text="选项3", variable=radio_var, value="选项3")
]
for button in radio_buttons:
    button.pack(anchor=tk.W, padx=10)

# 创建复选框组并放置在窗口上
checkbox_label = tk.Label(root, text="请选择一些复选框:")
checkbox_label.pack(pady=5)
checkboxes = {
    "复选框1": tk.IntVar(),
    "复选框2": tk.IntVar(),
    "复选框3": tk.IntVar()
}
checkbox_widgets = {}
for label_text, var in checkboxes.items():
    checkbox = tk.Checkbutton(root, text=label_text, variable=var)
    checkbox.pack(anchor=tk.W, padx=10)
    checkbox_widgets[label_text] = checkbox  # 可选：存储小部件引用以便后续访问

# 创建按钮并放置在窗口上
button = tk.Button(root, text="提交", command=on_button_click)
button.pack(pady=20)

# 运行主事件循环
root.mainloop()
