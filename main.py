from tkinter import *
from PIL import Image, ImageTk


class IndexWin:
    def __init__(self):
        self.width = 1024
        self.height = 600
        self.bg_color = '#39889f'
        self.min_width = 400
        self.min_height = 200

    def get_screen_size(self):
        """获取屏幕宽高"""
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        return screen_width, screen_height

    def get_center_location(self, width, height):
        """获取屏幕居中位置"""
        screen_width, screen_height = self.get_screen_size()
        return (screen_width - width) / 2, (screen_height - height) / 2

    def set_label_common(self, text):
        options = {
            'text': text,  # 文本内容
            'font': '楷体 14',  # 字体
            'fg': '#cee1e7',  # 前景色
            'bg': self.bg_color,  # 背景色
            'wraplength': self.min_width,  # 自动换行宽度设置
            'justify': 'left'  # 自动换行显示的最后与行居左对齐
        }
        return options


if __name__ == '__main__':
    win = IndexWin()
    root = Tk()
    root.title('such_test')  # 窗口标题
    x, y = win.get_center_location(win.width, win.height)
    root.geometry('%dx%d+%d+%d' % (win.width, win.height, x, y))  # 窗口宽高、位置
    root.configure(bg=win.bg_color)  # 窗口背景色
    # root.resizable(0, 0)   # 窗口不可更改大小
    root.maxsize(*win.get_screen_size())  # 设置窗口拖拽时的最大大小
    root.minsize(400, 200)  # 设置窗口拖拽时的最小大小
    # logo
    image = PhotoImage(file='static/image/logo.png')
    options = win.set_label_common('SUCH TEST')
    options['anchor'] = 'nw'
    label = Label(root, options, image=image,compound='left')
    label.pack()  # 包装与定位控件

    # image = Image.open('static/image/logo.png')
    # stone = ImageTk.PhotoImage(image)
    # options = win.set_label_common('SUCH TEST')
    # options['anchor'] = 'nw'
    # options['cursor'] = 'heart'  # 鼠标为心形
    # label = Label(root, options, image=stone,compound='left')  # compound使图像与文字共存
    label.pack(side=LEFT,anchor=NW)  # 包装与定位控件
    # login or register
    options = win.set_label_common('登录')
    label = Label(root, options)
    label.pack(side=RIGHT,anchor=NE)  # 包装与定位控件

    root.mainloop()
