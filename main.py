import tkinter as tk
from tkinter import filedialog, messagebox, colorchooser
import cv2
import threading
import time
import datetime
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import tkinter.font as tkFont

STYLE_CONFIG = {
    "bg": "#FFE4C4",
    "fg": "#8B4513",
    "danger": "#FF4444",
    "success": "#44FF44",
    "font": ("Consolas", 6),
}


class SetupDlg:
    def __init__(self, parent):
        self.parent = parent
        self.cfg = None
        self.root = ttk.Toplevel(parent)
        self.root.title("视频设置")
        self.root.geometry("650x265")
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        self.root.grab_set()

        self.build_ui()
        self.root.wait_window()

    def build_ui(self):
        main = ttk.Frame(self.root, padding=15)
        main.pack(expand=True, fill=tk.BOTH)

        # 帧率设置
        ttk.Label(main, text="帧率:").grid(row=0, column=0, sticky=tk.W, pady=10)
        self.fps_val = tk.StringVar(value="原视频")
        opts = ["原视频", "24 (电影)", "30 (普通)", "60 (高速)", "自定义"]
        self.fps_box = ttk.Combobox(
            main, textvariable=self.fps_val, values=opts, width=18, bootstyle="info"
        )
        self.fps_box.grid(row=0, column=1, columnspan=2, sticky=tk.EW, padx=5)
        self.fps_box.bind("<<ComboboxSelected>>", self.fps_chg)
        self.fps_in = ttk.Entry(main, width=12, state=tk.DISABLED)
        self.fps_in.grid(row=0, column=3, padx=5)

        # 分辨率设置
        ttk.Label(main, text="分辨率:").grid(row=1, column=0, sticky=tk.W, pady=15)
        self.res_val = tk.StringVar(value="自动调整")
        res_opts = [
            "自动调整",
            "低 (200x112)",
            "中 (240x135)",
            "高 (280x158)",
            "自定义",
        ]
        self.res_box = ttk.Combobox(
            main, textvariable=self.res_val, values=res_opts, width=18, bootstyle="info"
        )
        self.res_box.grid(row=1, column=1, columnspan=2, sticky=tk.EW, padx=5)
        self.res_box.bind("<<ComboboxSelected>>", self.res_chg)
        self.w_in = ttk.Entry(main, width=8, state=tk.DISABLED)
        self.w_in.grid(row=1, column=3, padx=2)
        ttk.Label(main, text="×").grid(row=1, column=4)
        self.h_in = ttk.Entry(main, width=8, state=tk.DISABLED)
        self.h_in.grid(row=1, column=5, padx=2)

        # 字符大小设置
        ttk.Label(main, text="字符大小:").grid(row=2, column=0, sticky=tk.W, pady=15)
        self.size_val = tk.StringVar(value="自动调整")
        size_opts = ["自动调整", "小 (4pt)", "中 (6pt)", "大 (8pt)", "自定义"]
        self.size_box = ttk.Combobox(
            main, textvariable=self.size_val, values=size_opts, width=18, bootstyle="info"
        )
        self.size_box.grid(row=2, column=1, columnspan=2, sticky=tk.EW, padx=5)
        self.size_box.bind("<<ComboboxSelected>>", self.size_chg)
        self.size_in = ttk.Entry(main, width=12, state=tk.DISABLED)
        self.size_in.grid(row=2, column=3, padx=5)

        # 确认按钮组
        btn_frame = ttk.Frame(main)
        btn_frame.grid(row=3, column=0, columnspan=6, pady=20)
        ttk.Button(
            btn_frame,
            text="确认",
            command=self.ok,
            bootstyle="success-outline",
            width=12,
        ).pack(side=tk.LEFT, padx=8)
        ttk.Button(
            btn_frame,
            text="取消",
            command=self.cancel,
            bootstyle="danger-outline",
            width=12,
        ).pack(side=tk.LEFT, padx=8)

    def fps_chg(self, _=None):
        self.fps_in.config(
            state=tk.NORMAL if self.fps_val.get() == "自定义" else tk.DISABLED
        )

    def res_chg(self, _=None):
        state = tk.NORMAL if self.res_val.get() == "自定义" else tk.DISABLED
        self.w_in.config(state=state)
        self.h_in.config(state=state)

    def size_chg(self, _=None):
        self.size_in.config(
            state=tk.NORMAL if self.size_val.get() == "自定义" else tk.DISABLED
        )

    def check(self):
        cfg = {"fps": 30, "w": 240, "h": 135, "font_size": 6}  # 默认字号设为6
        try:
            # 帧率校验
            if self.fps_val.get() == "自定义":
                if not self.fps_in.get().isdigit():
                    raise ValueError("帧率必须为数字")
                cfg["fps"] = int(self.fps_in.get())
                if cfg["fps"] <= 0:
                    raise ValueError("帧率必须大于0")

            # 分辨率校验
            if self.res_val.get() == "自定义":
                if not (self.w_in.get().isdigit() and self.h_in.get().isdigit()):
                    raise ValueError("分辨率必须为整数")
                cfg["w"] = int(self.w_in.get())
                cfg["h"] = int(self.h_in.get())
                if cfg["w"] <= 0 or cfg["h"] <= 0:
                    raise ValueError("分辨率必须大于0")

            # 字体大小校验
            if self.size_val.get() == "自定义":
                if not self.size_in.get().isdigit():
                    raise ValueError("抱歉，字号必须为整数")
                cfg["font_size"] = int(self.size_in.get())
                if not (4 <= cfg["font_size"] <= 12):
                    raise ValueError("请注意，字号需在4-12之间")

        except ValueError as e:
            messagebox.showerror("输入错误", f"参数错误: {str(e)}")
            return None
        return cfg

    def ok(self):
        if cfg := self.check():
            self.cfg = cfg
            self.root.grab_release()
            self.root.destroy()

    def cancel(self):
        self.cfg = {"fps": 30, "w": 240, "h": 135, "font_size": 6}  # 默认值
        self.root.grab_release()
        self.root.destroy()

    def close(self):
        if messagebox.askokcancel("退出", "确定取消？"):
            self.cancel()


class VideoConverter:
    def __init__(self, root, settings):
        self.root = root
        self.settings = settings
        self.setup_ui()
        self.init_vars()
        self.bind_events()
        self.check_special_time()

    def open_settings(self):
        settings = SetupDlg(self.root).cfg
        return settings

    def setup_ui(self):
        self.root.title("ASCII视频转换器 V3.0.1 (beta) 🐾")
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # 控制面板
        self.ctrl_frame = ttk.Labelframe(
            self.main_frame, text="控制台", bootstyle="info"
        )
        self.ctrl_frame.pack(fill=tk.X, padx=10, pady=5)

        self.create_buttons()
        self.create_display()
        self.create_status_bar()

    def init_vars(self):
        self.video_path = ""
        self.cap = None
        self.is_playing = False
        self.is_paused = False
        self.frame_count = 0
        self.total_frames = 0
        self.title_clicks = 0
        self.last_click_time = 0
        # 使用设置对话框中指定的字体大小（默认为6）
        self.font_size = self.settings.get("font_size", 6)
        # 固定样式中字体也更新为该大小
        STYLE_CONFIG["font"] = ("Consolas", self.font_size)

    def bind_events(self):
        self.root.bind("<Button-1>", self.on_title_click)
        self.root.bind("<space>", self.toggle_pause)
        self.root.bind("<Escape>", self.exit_app)
        self.display.bind("<Double-Button-1>", self.toggle_theme)
        # 当窗口尺寸变化时，重新生成 ASCII 图像
        self.root.bind("<Configure>", self.on_resize)

    def create_buttons(self):
        help_btn = ttk.Button(self.ctrl_frame, text="帮助", width=10)
        help_btn.pack(side=tk.LEFT, padx=5)
        help_btn.bind("<Button-1>", self.show_help)
        ttk.Button(
            self.ctrl_frame, text="背景色", command=self.change_bg_color, width=10
        ).pack(side=tk.LEFT, padx=5)
        # 保存“打开视频”按钮
        self.btn_open = ttk.Button(
            self.ctrl_frame, text="打开视频", command=self.open_video, width=10
        )
        self.btn_open.pack(side=tk.LEFT, padx=5)
        self.btn_start = ttk.Button(
            self.ctrl_frame,
            text="开始",
            state=tk.DISABLED,
            command=self.start_conversion,
            width=10,
        )
        self.btn_start.pack(side=tk.LEFT, padx=5)
        # 将“停止”按钮改为“清空画布”，默认禁用
        self.btn_clear = ttk.Button(
            self.ctrl_frame,
            text="清空画布",
            state=tk.DISABLED,
            command=self.clear_canvas,
            width=10,
        )
        self.btn_clear.pack(side=tk.LEFT, padx=5)

    def show_help(self, event=None):
        if event and event.state & 0x0001:  # 检查Shift键
            dev_info = [
                "---灵曦工作室---",
                "版本：V3.0.1 (beta)",
                "引擎版本：LX引擎1.0",
            ]
            messagebox.showinfo("信息", "\n".join(dev_info))
        else:
            help_window = tk.Toplevel(self.root)
            help_window.title("帮助")
            help_window.geometry("500x530")

            # 帮助文本
            help_text = """
                          帮助手册
          - 背景色 ：自定义背景颜色
          - 打开视频：导入需转换的视频
          - 开始/清空画布：控制转换进程
          快捷键：  
          * 空格键：暂停/继续
          * Esc键：退出程序
            """
            help_label = ttk.Label(
                help_window, text=help_text, wraplength=380, justify=tk.LEFT
            )
            help_label.pack(pady=10)

            bilibili_link = ttk.Label(
                help_window, text="哔哩哔哩：@玩摄影的程序猿", foreground="blue", cursor="hand2"
            )
            bilibili_link.pack()
            bilibili_link.bind(
                "<Button-1>",
                lambda event: self.open_link("https://space.bilibili.com/3537122176797008?spm_id_from=333.1007.0.0")
            )

            # GitHub链接
            github_text = "项目Github地址："
            github_label = ttk.Label(
                help_window, text=github_text, wraplength=380, justify=tk.LEFT
            )
            github_label.pack()

            github_link = ttk.Label(
                help_window, text=">点击前往<", foreground="blue", cursor="hand2"
            )
            github_link.pack()
            github_link.bind(
                "<Button-1>",
                lambda event: self.open_link("https://github.com/huqingyuan-Python/Video-to-ASCII-art")
            )

            # 底部说明
            bottom_text = "本程序严禁用于商业用途"
            bottom_label = ttk.Label(
                help_window, text=bottom_text, wraplength=380, justify=tk.LEFT
            )
            bottom_label.pack(pady=10)

    def open_link(self, url):
        import webbrowser
        webbrowser.open(url)

    def create_display(self):
        self.display = tk.Text(
            self.main_frame,
            font=STYLE_CONFIG["font"],
            bg=STYLE_CONFIG["bg"],
            fg=STYLE_CONFIG["fg"],
            wrap=tk.NONE,
        )
        self.display.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        # 窗口尺寸变化时由 on_resize 重新生成 ASCII 图像
        self.display.bind("<Configure>", self.on_resize)

    def on_resize(self, event=None):
        # 当窗口或文本控件尺寸变化时，根据当前文本控件尺寸生成 ASCII 图像
        if self.cap and event and event.widget == self.display:
            frame = self.get_current_frame()
            if frame is not None:
                ascii_art = self.generate_ascii(frame)
                self.update_display(ascii_art)

    def generate_ascii(self, frame):
        # 转换为灰度图
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # 获取文本控件实际像素尺寸
        widget_width = self.display.winfo_width()
        widget_height = self.display.winfo_height()

        # 使用固定字体度量信息（字体大小已固定为6）
        current_font = tkFont.Font(font=STYLE_CONFIG["font"])
        char_width = current_font.measure("A")
        char_height = current_font.metrics("linespace")

        # 计算文本区域可容纳的字符列数和行数
        cols = max(1, widget_width // char_width)
        rows = max(1, widget_height // char_height)

        # 缩放灰度图到 (cols, rows) 大小
        small = cv2.resize(gray, (cols, rows))

        # 灰度值映射到 ASCII 字符
        chars = "@%#*+=-:. "
        ascii_art = "\n".join(
            "".join(
                chars[min(int(pixel / 255 * (len(chars) - 1)), len(chars) - 1)]
                for pixel in row
            )
            for row in small
        )
        return ascii_art

    def get_current_frame(self):
        # 获取当前帧
        ret, frame = self.cap.read()
        if ret:
            return frame
        return None

    def create_status_bar(self):
        self.status = ttk.Label(
            self.main_frame, text="就绪", anchor=tk.W, bootstyle="inverse-secondary"
        )
        self.status.pack(fill=tk.X, padx=10, pady=5)

    def check_special_time(self):
        now = datetime.datetime.now()
        weekday = now.weekday()  # 0=星期一，6=星期日
        hour = now.hour

        # 根据星期几显示不同祝福语
        if weekday == 0:
            self.status.config(text="星期一，新的开始！加油哦 🌟")
        elif weekday == 1:
            self.status.config(text="星期二，继续保持！💪")
        elif weekday == 2:
            self.status.config(text="星期三，已经过半啦！🎉")
        elif weekday == 3:
            self.status.config(text="星期四，快到周末啦！😎")
        elif weekday == 4:
            self.status.config(text="周五快乐哦！明天想去哪里放松呢 🎉")
        elif weekday == 5:
            self.status.config(text="星期六，好好享受周末吧！☀️")
        elif weekday == 6:
            self.status.config(text="星期日，放松一下，准备迎接新的一周！🌼")

        # 夜间模式（0-6点）
        if 0 <= hour < 6:
            self.enable_night_mode()

    def open_video(self):
        self.video_path = filedialog.askopenfilename()
        if self.video_path:
            self.init_video_capture()
            # 启用“开始”按钮
            self.btn_start.config(state=tk.NORMAL)
            # 导入视频后未开始转换，按钮显示“取消选择”
            self.btn_clear.config(state=tk.NORMAL, text="取消选择")
            self.update_status(f"已加载: {self.video_path.split('/')[-1]}")

    def init_video_capture(self):
        if self.cap:
            self.cap.release()
        self.cap = cv2.VideoCapture(self.video_path)
        self.total_frames = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))

    def start_conversion(self):
        try:
            if not self.cap or not self.cap.isOpened():
                raise ValueError("请先打开有效视频文件")

            self.is_playing = True
            # 开始转换后禁用“开始”和“打开视频”按钮
            self.btn_start.config(state=tk.DISABLED)
            self.btn_open.config(state=tk.DISABLED)
            # 转换状态下，按钮显示为“清空画布”
            self.btn_clear.config(text="清空画布")
            threading.Thread(target=self.process_frames, daemon=True).start()

        except Exception as e:
            messagebox.showerror("启动错误", f"无法开始转换: {str(e)}")
            self.clear_canvas()  # 出错时清空状态

    def process_frames(self):
        while self.is_playing and self.cap.isOpened():
            if not self.is_paused:
                ret, frame = self.cap.read()
                if ret:
                    ascii_art = self.generate_ascii(frame)
                    # 主线程更新界面
                    self.root.after(0, self.update_display, ascii_art)
                    self.root.after(0, self.update_progress)
                else:
                    # 视频播放完毕后停止
                    self.is_playing = False
            fps = self.settings.get("fps", 30)
            if fps is None or fps <= 0:
                fps = 30
            time.sleep(1 / fps)

    def update_display(self, art):
        self.display.delete(1.0, tk.END)
        self.display.insert(tk.END, art)

    def on_title_click(self, event):
        if event.y < 30:
            current_time = time.time()
            if current_time - self.last_click_time < 1.0:
                self.title_clicks += 1
                if self.title_clicks == 3:
                    self.show_secret_cat()
                    self.title_clicks = 0
            else:
                self.title_clicks = 1
            self.last_click_time = current_time

    def show_secret_cat(self):
        cat_art = r"""
     /\_/\  
    ( o.o ) 
     > ^ <  
                  ★ 感谢信 ★         
         ----------------------------------
                感谢打开本文件的你：  
             你的好奇心让这本喵充满动力！  
              感谢贡献过本项目的小可爱们：  
             你们的爪印让项目更加蓬松柔软~  
               感谢提出issue的团员们：  
          每一个bug报告都对这个项目有着推进作用  
                   最后特别感谢：  
            每一位喜欢毛茸茸的你 (๑>ᴗ<๑)"""
        messagebox.showinfo("致谢信", cat_art)

    def toggle_theme(self, event):
        current_bg = self.display.cget("bg")
        new_bg = "#FFB6C1" if current_bg == STYLE_CONFIG["bg"] else STYLE_CONFIG["bg"]
        new_fg = "#800080" if current_bg == STYLE_CONFIG["bg"] else STYLE_CONFIG["fg"]
        self.display.config(bg=new_bg, fg=new_fg)

    def enable_night_mode(self):
        self.display.config(bg="#1A1A1A", fg="#00FF00")
        self.display.tag_configure("sleep", foreground="#FF69B4")
        self.display.insert(tk.END, "\n(・ω・)zZzZ... 该休息了哦～", "sleep")

    def update_progress(self):
        self.frame_count += 1
        progress = f"{self.frame_count}/{self.total_frames}"
        self.status.config(text=f"进度: {progress} 🐾")

    def update_status(self, message):
        self.status.config(text=message)

    def toggle_pause(self, event=None):
        self.is_paused = not self.is_paused
        status = "已暂停" if self.is_paused else "播放中"
        self.update_status(f"{status} ⏸️" if self.is_paused else f"{status} ▶️")

    def stop(self):
        self.is_playing = False
        try:
            if self.cap and self.cap.isOpened():
                self.cap.release()
        except Exception as e:
            print(f"释放视频资源时出错: {str(e)}")
        finally:
            self.btn_clear.config(state=tk.NORMAL)
            self.update_status("已停止 ⏹️")

    def clear_canvas(self):
        """
        根据当前状态执行：
         - 如果视频已开始转换（转换中），则停止转换、清空输出面板、重置视频选择，
           启用“打开视频”按钮，同时保持“开始”按钮禁用（需重新选择视频）。
         - 如果视频仅被选择但未开始转换，则取消视频选择、清空输出面板，
           并禁用“开始”和“清空画布”按钮。
        """
        if self.is_playing:
            # 正在转换状态下，先停止转换
            self.stop()
            self.display.delete("1.0", tk.END)
            self.video_path = ""
            self.btn_open.config(state=tk.NORMAL)
            self.btn_start.config(state=tk.DISABLED)
            self.btn_clear.config(state=tk.DISABLED)
            self.update_status("已清空画布")
        else:
            # 未开始转换时，即“取消选择”状态
            self.video_path = ""
            if self.cap:
                self.cap.release()
                self.cap = None
            self.display.delete("1.0", tk.END)
            self.btn_start.config(state=tk.DISABLED)
            self.btn_clear.config(state=tk.DISABLED)
            self.update_status("已取消视频选择")

    def exit_app(self, event=None):
        self.stop()
        self.root.destroy()

    def change_bg_color(self):
        color = colorchooser.askcolor(
            title="选择背景色", initialcolor=STYLE_CONFIG["bg"]
        )
        if color[1]:
            self.display.config(bg=color[1])


if __name__ == "__main__":
    root = ttk.Window(title="ASCII视频转换器", themename="pulse")
    root.withdraw()

    # 启动视频设置窗口
    setup = SetupDlg(root)
    settings = setup.cfg

    # 判断并启动主应用程序
    if settings:
        root.deiconify()
        app = VideoConverter(root, settings)
        root.mainloop()
