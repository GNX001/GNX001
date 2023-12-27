import tkinter as tk
from tkinter import StringVar
from datetime import datetime, timedelta

def validate_numeric_input(value, entry_widget):
    # 验证输入是否为数字
    if value.isdigit() or (value.startswith('-') and value[1:].isdigit()):
        return True
    else:
        result_label.config(text="请输入有效的数字", fg="red")
        entry_widget.delete(0, tk.END)
        return False

def set_current_time(entry_widgets):
    # 将当前时间填写到对应的输入框中
    current_time = datetime.now()
    for entry_widget, part in zip(entry_widgets, [current_time.year, current_time.month, current_time.day, current_time.hour, current_time.minute, current_time.second]):
        entry_widget.delete(0, tk.END)
        entry_widget.insert(0, str(part))
    
    update_info_label("先后点击鼠标左、右键即可复制计算结果")

def calculate_timediff(*args):
    try:
        # 获取用户输入的年月日时分秒
        year = int(entry_year_var.get())
        month = int(entry_month_var.get())
        day = int(entry_day_var.get())
        hour = int(entry_hour_var.get())
        minute = int(entry_minute_var.get())
        second = int(entry_second_var.get())

        # 检查输入的合法性
        if not (1 <= month <= 12 and 1 <= day <= 31 and 0 <= hour < 24 and 0 <= minute < 60 and 0 <= second < 60):
            raise ValueError("输入的日期或时间不合法")

        # 构建开始时间和结束时间的datetime对象
        start_time = datetime(year, month, day, hour, minute, second)

        end_year = int(entry_end_year_var.get())
        end_month = int(entry_end_month_var.get())
        end_day = int(entry_end_day_var.get())
        end_hour = int(entry_end_hour_var.get())
        end_minute = int(entry_end_minute_var.get())
        end_second = int(entry_end_second_var.get())

        # 检查输入的合法性
        if not (1 <= end_month <= 12 and 1 <= end_day <= 31 and 0 <= end_hour < 24 and 0 <= end_minute < 60 and 0 <= end_second < 60):
            raise ValueError("输入的日期或时间不合法")

        end_time = datetime(end_year, end_month, end_day, end_hour, end_minute, end_second)

        # 计算时间差
        time_difference = end_time - start_time

        # 格式化计算结果，使用中文时间单位
        result_text = f"时间差：{time_difference.days}天 {time_difference.seconds // 3600}小时 {time_difference.seconds % 3600 // 60}分钟 {time_difference.seconds % 60}秒"
        result_label.config(text=result_text, fg="black")

        update_info_label("先后点击鼠标左、右键即可复制计算结果")

    except ValueError as e:
        result_label.config(text=str(e), fg="red")
        update_info_label("先后点击鼠标左、右键即可复制计算结果")

def update_info_label(*args):
    info_label.config(text="先后点击鼠标左、右键即可复制计算结果", fg="black")

# 复制成功提示
def copy_success():
    result_label.config(text="复制成功！", fg="red")
    root.after(3000, update_info_label)  # 3秒后清空提示信息

# 更新提示信息标签
def update_info_label(*args):
    info_label.config(text="先后点击鼠标左、右键即可复制计算结果", fg="black")



# 创建主窗口
root = tk.Tk()
root.title("时差计算器——本计算器由“没有轨道的彗星”提供创意，由GPT3.5编写代码！")

# 创建输入框和标签
entry_width = 6

entry_year_var = StringVar()
entry_year_var.trace_add("write", update_info_label)

entry_year = tk.Entry(root, width=entry_width, textvariable=entry_year_var)
entry_year.config(validate="key", validatecommand=(root.register(lambda s: validate_numeric_input(s, entry_year)), '%P'))
label_year = tk.Label(root, text="年")

entry_month_var = StringVar()
entry_month_var.trace_add("write", update_info_label)

entry_month = tk.Entry(root, width=entry_width, textvariable=entry_month_var)
entry_month.config(validate="key", validatecommand=(root.register(lambda s: validate_numeric_input(s, entry_month)), '%P'))
label_month = tk.Label(root, text="月")

entry_day_var = StringVar()
entry_day_var.trace_add("write", update_info_label)

entry_day = tk.Entry(root, width=entry_width, textvariable=entry_day_var)
entry_day.config(validate="key", validatecommand=(root.register(lambda s: validate_numeric_input(s, entry_day)), '%P'))
label_day = tk.Label(root, text="日")

entry_hour_var = StringVar()
entry_hour_var.trace_add("write", update_info_label)

entry_hour = tk.Entry(root, width=entry_width, textvariable=entry_hour_var)
entry_hour.config(validate="key", validatecommand=(root.register(lambda s: validate_numeric_input(s, entry_hour)), '%P'))
label_hour = tk.Label(root, text="小时")

entry_minute_var = StringVar()
entry_minute_var.trace_add("write", update_info_label)

entry_minute = tk.Entry(root, width=entry_width, textvariable=entry_minute_var)
entry_minute.config(validate="key", validatecommand=(root.register(lambda s: validate_numeric_input(s, entry_minute)), '%P'))
label_minute = tk.Label(root, text="分钟")

entry_second_var = StringVar()
entry_second_var.trace_add("write", update_info_label)

entry_second = tk.Entry(root, width=entry_width, textvariable=entry_second_var)
entry_second.config(validate="key", validatecommand=(root.register(lambda s: validate_numeric_input(s, entry_second)), '%P'))
label_second = tk.Label(root, text="秒")

label_start_time = tk.Label(root, text="开始时间:")

entry_end_year_var = StringVar()
entry_end_year_var.trace_add("write", update_info_label)

entry_end_year = tk.Entry(root, width=entry_width, textvariable=entry_end_year_var)
entry_end_year.config(validate="key", validatecommand=(root.register(lambda s: validate_numeric_input(s, entry_end_year)), '%P'))
label_end_year = tk.Label(root, text="年")

entry_end_month_var = StringVar()
entry_end_month_var.trace_add("write", update_info_label)

entry_end_month = tk.Entry(root, width=entry_width, textvariable=entry_end_month_var)
entry_end_month.config(validate="key", validatecommand=(root.register(lambda s: validate_numeric_input(s, entry_end_month)), '%P'))
label_end_month = tk.Label(root, text="月")

entry_end_day_var = StringVar()
entry_end_day_var.trace_add("write", update_info_label)

entry_end_day = tk.Entry(root, width=entry_width, textvariable=entry_end_day_var)
entry_end_day.config(validate="key", validatecommand=(root.register(lambda s: validate_numeric_input(s, entry_end_day)), '%P'))
label_end_day = tk.Label(root, text="日")

entry_end_hour_var = StringVar()
entry_end_hour_var.trace_add("write", update_info_label)

entry_end_hour = tk.Entry(root, width=entry_width, textvariable=entry_end_hour_var)
entry_end_hour.config(validate="key", validatecommand=(root.register(lambda s: validate_numeric_input(s, entry_end_hour)), '%P'))
label_end_hour = tk.Label(root, text="小时")

entry_end_minute_var = StringVar()
entry_end_minute_var.trace_add("write", update_info_label)

entry_end_minute = tk.Entry(root, width=entry_width, textvariable=entry_end_minute_var)
entry_end_minute.config(validate="key", validatecommand=(root.register(lambda s: validate_numeric_input(s, entry_end_minute)), '%P'))
label_end_minute = tk.Label(root, text="分钟")

entry_end_second_var = StringVar()
entry_end_second_var.trace_add("write", update_info_label)

entry_end_second = tk.Entry(root, width=entry_width, textvariable=entry_end_second_var)
entry_end_second.config(validate="key", validatecommand=(root.register(lambda s: validate_numeric_input(s, entry_end_second)), '%P'))
label_end_second = tk.Label(root, text="秒")

label_end_time = tk.Label(root, text="结束时间:")

# 创建计算按钮
calculate_button = tk.Button(root, text="计算时差", command=calculate_timediff)

# 创建结果标签
result_label = tk.Label(root, text="", font=("Arial", 12), wraplength=500)

# 创建设置当前时间按钮（第一行）
set_current_time_button_row1 = tk.Button(root, text="设置为当前时间", command=lambda: set_current_time([entry_year, entry_month, entry_day, entry_hour, entry_minute, entry_second]))

# 创建设置当前时间按钮（第二行）
set_current_time_button_row2 = tk.Button(root, text="设置为当前时间", command=lambda: set_current_time([entry_end_year, entry_end_month, entry_end_day, entry_end_hour, entry_end_minute, entry_end_second]))

# 提示信息标签
info_label = tk.Label(root, text="先后点击鼠标左、右键即可复制计算结果", font=("Arial", 10), fg="black")

# 布局界面
label_start_time.grid(row=0, column=0, pady=5)
entry_year.grid(row=1, column=0, padx=5)
label_year.grid(row=1, column=1)

entry_month.grid(row=1, column=2, padx=5)
label_month.grid(row=1, column=3)

entry_day.grid(row=1, column=4, padx=5)
label_day.grid(row=1, column=5)

entry_hour.grid(row=1, column=6, padx=5)
label_hour.grid(row=1, column=7)

entry_minute.grid(row=1, column=8, padx=5)
label_minute.grid(row=1, column=9)

entry_second.grid(row=1, column=10, padx=5)
label_second.grid(row=1, column=11)

set_current_time_button_row1.grid(row=1, column=12, pady=5)

label_end_time.grid(row=2, column=0, pady=5)
entry_end_year.grid(row=3, column=0, padx=5)
label_end_year.grid(row=3, column=1)

entry_end_month.grid(row=3, column=2, padx=5)
label_end_month.grid(row=3, column=3)

entry_end_day.grid(row=3, column=4, padx=5)
label_end_day.grid(row=3, column=5)

entry_end_hour.grid(row=3, column=6, padx=5)
label_end_hour.grid(row=3, column=7)

entry_end_minute.grid(row=3, column=8, padx=5)
label_end_minute.grid(row=3, column=9)

entry_end_second.grid(row=3, column=10, padx=5)
label_end_second.grid(row=3, column=11)

calculate_button.grid(row=4, column=0, columnspan=6, pady=10)
result_label.grid(row=4, column=6, columnspan=6, pady=10)

set_current_time_button_row2.grid(row=3, column=12, pady=5)

info_label.grid(row=5, column=0, columnspan=12, pady=5)

# 让结果标签支持文本复制
result_label.bind("<ButtonPress-1>", lambda e: result_label.select_range(0, tk.END))
result_label.bind("<ButtonPress-3>", lambda e: root.clipboard_clear() or root.clipboard_append(result_label.cget("text")) or copy_success())

# 提示信息标签
info_label.grid(row=6, column=0, columnspan=12, pady=5)

# 进入主循环
root.mainloop()
