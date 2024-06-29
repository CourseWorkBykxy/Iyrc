from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import IyrcManager

m = IyrcManager.IyrcManager()


def cleanFrame(frame):
    for child in frame.winfo_children():
        child.destroy()


class IyrcUI():
    def __init__(self, root):
        # 初始化
        self.root = root
        self.root.title("墨韵读书会")
        self.frame = Frame(self.root)
        self.frame.pack(padx=10, pady=10)
        self.f1 = Frame(self.root)
        self.f1.pack(padx=10, pady=10)
        self.f2 = Frame(self.root)
        self.f2.pack(padx=10, pady=10)

        # 一些控件
        self.message = Entry(self.frame, textvariable=StringVar())
        self.username = Entry(self.frame, textvariable=StringVar())
        self.password = Entry(self.frame, textvariable=StringVar())
        self.password2 = Entry(self.frame, textvariable=StringVar())
        self.email = Entry(self.frame, textvariable=StringVar())
        self.type = Entry(self.frame, textvariable=StringVar())

        self.blogID = Entry(self.f1, textvariable=StringVar())
        self.blogid = Entry(self.f2, textvariable=StringVar())
        self.blogtitle = Entry(self.f2, textvariable=StringVar())
        self.author = Entry(self.f2, textvariable=StringVar())
        self.blogcreatetime = Entry(self.f2, textvariable=StringVar())
        self.blogupdatetime = Entry(self.f2, textvariable=StringVar())
        self.blogtext = Text(self.f2, width=45, height=15)

    def size1(self):
        # 窗口居中
        screenWidth = self.root.winfo_screenwidth()  # 获取显示区域的宽度
        screenHeight = self.root.winfo_screenheight()  # 获取显示区域的高度
        width = 360  # 设定窗口宽度
        height = 200  # 设定窗口高度
        left = (screenWidth - width) / 2
        top = (screenHeight - height) / 2
        self.root.geometry("%dx%d+%d+%d" % (width, height, left, top))

    def size2(self):
        # 窗口居中
        screenWidth = self.root.winfo_screenwidth()  # 获取显示区域的宽度
        screenHeight = self.root.winfo_screenheight()  # 获取显示区域的高度
        width = 1440  # 设定窗口宽度
        height = 900  # 设定窗口高度
        left = (screenWidth - width) / 2
        top = (screenHeight - height) / 2
        self.root.geometry("%dx%d+%d+%d" % (width, height, left, top))

    def userMain(self):
        cleanFrame(self.frame)
        cleanFrame(self.f1)
        cleanFrame(self.f2)
        self.size2()
        Label(self.frame, text='主菜单选择:').grid(row=1, column=0, padx=5)
        Button(self.frame, text='个人信息管理', command=self.userInfo).grid(row=1, column=1, pady=5)
        Button(self.frame, text='博客信息管理', command=self.blogManage).grid(row=1, column=2, pady=5)
        Button(self.frame, text='书籍信息管理', command=self.bookManage).grid(row=1, column=3, pady=5)
        Button(self.frame, text='退出', command=self.login).grid(row=1, column=4, pady=5)
        Label(self.frame, text='消息:').grid(row=3, column=0, padx=5)
        self.message = Entry(self.frame, textvariable=StringVar())
        self.message.grid(row=3, column=1, padx=5)

    def userInfo(self):
        cleanFrame(self.f1)
        cleanFrame(self.f2)
        Label(self.f1, text='当前菜单:个人信息管理').grid(row=0, column=0, padx=5)
        Label(self.f1, text='功能选择:').grid(row=1, column=0, padx=5)
        Button(self.f1, text='显示个人信息', command=lambda: m.showUserInfo(self)).grid(row=1, column=1, pady=5)
        Button(self.f1, text='修改个人信息', command=lambda: m.updateUserInfo(self)).grid(row=1, column=2, pady=5)
        Label(self.f1, text='个人信息').grid(row=2, column=0, padx=5)
        Label(self.f1, text='用户名:').grid(row=3, column=0, padx=5)
        Label(self.f1, text='密码:').grid(row=4, column=0, padx=5)
        Label(self.f1, text='邮箱:').grid(row=5, column=0, padx=5)
        Label(self.f1, text='用户类型:').grid(row=6, column=0, padx=5)
        self.username = Entry(self.f1, textvariable=StringVar())
        self.password = Entry(self.f1, textvariable=StringVar())
        self.email = Entry(self.f1, textvariable=StringVar())
        self.type = Entry(self.f1, textvariable=StringVar())
        self.username.grid(row=3, column=1, padx=5)
        self.password.grid(row=4, column=1, padx=5)
        self.email.grid(row=5, column=1, padx=5)
        self.type.grid(row=6, column=1, padx=5)

    def blogManage(self):
        cleanFrame(self.f1)
        cleanFrame(self.f2)
        Label(self.f1, text='当前菜单:博客信息管理').grid(row=0, column=0, padx=5)
        Label(self.f1, text='功能选择:').grid(row=1, column=0, padx=5)
        Button(self.f1, text='浏览博客', command=self.toScanBlog).grid(row=1, column=1, pady=5)
        Button(self.f1, text='我的博客', command=lambda: m.selectMyBlog(self)).grid(row=1, column=2, pady=5)
        Button(self.f1, text='创建博客', command=self.toCreateBlog).grid(row=1, column=3, pady=5)
        Label(self.f1, text='希望查看的博客ID:').grid(row=2, column=0, padx=5)
        self.blogID = Entry(self.f1, textvariable=StringVar())
        self.blogID.grid(row=2, column=1, padx=5)
        Button(self.f1, text='查看', command=lambda: m.selectBlog(self)).grid(row=2, column=2, pady=5)

    def toMyBlog(self):
        cleanFrame(self.f2)
        # 创建表格对象
        self.tree = ttk.Treeview(self.f2)
        # 定义列
        self.tree["columns"] = ("标题", "作者", "创建时间", "最后修改时间")
        self.tree.column("标题", width=200)
        self.tree.column("作者", width=100)
        self.tree.column("创建时间", width=150)
        self.tree.column("最后修改时间", width=150)
        # 设置显示的表头名
        self.tree.heading("标题", text="标题")
        self.tree.heading("作者", text="作者")
        self.tree.heading("创建时间", text="创建时间")
        self.tree.heading("最后修改时间", text="最后修改时间")

    def toCreateBlog(self):
        cleanFrame(self.f2)
        Label(self.f2, text='博客信息').grid(row=0, column=0, padx=5)
        Label(self.f2, text='标题:').grid(row=2, column=0, padx=5)
        Label(self.f2, text='内容:').grid(row=6, column=0, padx=5)
        self.blogtitle = Entry(self.f2, textvariable=StringVar())
        self.blogtext = Text(self.f2, width=45, height=15)
        self.blogtitle.grid(row=2, column=1, padx=5)
        self.blogtext.grid(row=6, column=1, padx=5)
        Button(self.f2, text='创建', command=lambda: m.insertBlog(self)).grid(row=7, column=0, pady=5)



    def toScanBlog(self):
        cleanFrame(self.f2)
        # 创建表格对象
        tree = ttk.Treeview(self.f2)
        # 定义列
        tree["columns"] = ("标题", "作者", "创建时间", "最后修改时间")
        tree.column("标题", width=200)
        tree.column("作者", width=100)
        tree.column("创建时间", width=150)
        tree.column("最后修改时间", width=150)
        # 设置显示的表头名
        tree.heading("标题", text="标题")
        tree.heading("作者", text="作者")
        tree.heading("创建时间", text="创建时间")
        tree.heading("最后修改时间", text="最后修改时间")
        m.db.open()
        cursor = m.db.selectAllBlog()
        for i in cursor:
            tree.insert("", i[0], text=str(i[0]), values=(i[1], i[2], i[3], i[4]))
        m.db.close()
        tree.pack()

    def toSelectBlog(self):
        cleanFrame(self.f2)
        Label(self.f2, text='博客信息').grid(row=0, column=0, padx=5)
        Label(self.f2, text='ID:').grid(row=1, column=0, padx=5)
        Label(self.f2, text='标题:').grid(row=2, column=0, padx=5)
        Label(self.f2, text='作者:').grid(row=3, column=0, padx=5)
        Label(self.f2, text='创建时间:').grid(row=4, column=0, padx=5)
        Label(self.f2, text='最后修改时间:').grid(row=5, column=0, padx=5)
        Label(self.f2, text='内容:').grid(row=6, column=0, padx=5)
        self.blogid = Entry(self.f2, textvariable=StringVar())
        self.blogtitle = Entry(self.f2, textvariable=StringVar())
        self.author = Entry(self.f2, textvariable=StringVar())
        self.blogcreatetime = Entry(self.f2, textvariable=StringVar())
        self.blogupdatetime = Entry(self.f2, textvariable=StringVar())
        self.blogtext = Text(self.f2, width=45, height=15)
        self.blogid.grid(row=1, column=1, padx=5)
        self.blogtitle.grid(row=2, column=1, padx=5)
        self.author.grid(row=3, column=1, padx=5)
        self.blogcreatetime.grid(row=4, column=1, padx=5)
        self.blogupdatetime.grid(row=5, column=1, padx=5)
        self.blogtext.grid(row=6, column=1, padx=5)

    def bookManage(self):
        cleanFrame(self.f1)
        cleanFrame(self.f2)
        Label(self.f1, text='当前菜单:书籍信息管理').grid(row=0, column=0, padx=5)
        Label(self.f1, text='功能选择:').grid(row=1, column=0, padx=5)
        Button(self.f1, text='查看书籍信息', command=self.toScanBook).grid(row=1, column=1, pady=5)
        Button(self.f1, text='查看书架信息', command=lambda: m.selectMyBook(self)).grid(row=1, column=2, pady=5)
        Label(self.f1, text='书籍ID:').grid(row=2, column=0, padx=5)
        self.bookID = Entry(self.f1, textvariable=StringVar())
        self.bookID.grid(row=2, column=1, padx=5)
        Button(self.f1, text='添加书籍', command=lambda: m.insertMyBook(self)).grid(row=2, column=2, pady=5)
        Button(self.f1, text='删除书籍', command=lambda: m.deleteMyBook(self)).grid(row=2, column=3, pady=5)

    def toMyBook(self):
        cleanFrame(self.f2)
        # 创建表格对象
        self.tree = ttk.Treeview(self.f2)
        # 定义列
        self.tree["columns"] = ("书名", "作者")
        self.tree.column("书名", width=200)
        self.tree.column("作者", width=100)
        # 设置显示的表头名
        self.tree.heading("书名", text="书名")
        self.tree.heading("作者", text="作者")


    def toScanBook(self):
        cleanFrame(self.f2)
        # 创建表格对象
        self.tree = ttk.Treeview(self.f2)
        # 定义列
        # 定义列
        self.tree["columns"] = ("书名", "作者")
        self.tree.column("书名", width=200)
        self.tree.column("作者", width=100)
        # 设置显示的表头名
        self.tree.heading("书名", text="书名")
        self.tree.heading("作者", text="作者")
        m.db.open()
        cursor = m.db.selectAllBook()
        for i in cursor:
            self.tree.insert("", i[0], text=str(i[0]), values=(i[1], i[2]))
        m.db.close()
        self.tree.pack()


    def login(self):
        cleanFrame(self.frame)
        cleanFrame(self.f1)
        self.size1()
        Label(self.frame, text='用户名:').grid(row=0, column=0, padx=5)
        Label(self.frame, text='密码:').grid(row=1, column=0, padx=5)
        self.username = Entry(self.frame, textvariable=StringVar())
        self.password = Entry(self.frame, textvariable=StringVar())
        self.username.grid(row=0, column=1, padx=5)
        self.password.grid(row=1, column=1, padx=5)
        Label(self.f1, text='消息:').grid(row=0, column=0, padx=5)
        self.message = Entry(self.f1, textvariable=StringVar())
        self.message.grid(row=0, column=1, padx=5)
        Button(self.f1, text='前往注册', command=self.register).grid(row=1, column=0, pady=5)
        Button(self.f1, text='登录', command=lambda: m.login(self)).grid(row=1, column=2, pady=5)

    def register(self):
        cleanFrame(self.frame)
        cleanFrame(self.f1)
        self.size1()
        Label(self.frame, text='用户名:').grid(row=0, column=0, padx=5)
        Label(self.frame, text='密码:').grid(row=1, column=0, padx=5)
        Label(self.frame, text='确认密码:').grid(row=2, column=0, padx=5)
        Label(self.frame, text='邮箱:').grid(row=3, column=0, padx=5)
        self.username = Entry(self.frame, textvariable=StringVar())
        self.password = Entry(self.frame, textvariable=StringVar())
        self.password2 = Entry(self.frame, textvariable=StringVar())
        self.email = Entry(self.frame, textvariable=StringVar())
        self.username.grid(row=0, column=1, padx=5)
        self.password.grid(row=1, column=1, padx=5)
        self.password2.grid(row=2, column=1, padx=5)
        self.email.grid(row=3, column=1, padx=5)

        Label(self.f1, text='消息:').grid(row=1, column=0, padx=5)
        self.message = Entry(self.f1, textvariable=StringVar())
        self.message.grid(row=1, column=1, padx=5)
        Button(self.f1, text='注册', command=lambda: m.register(self)).grid(row=4, column=0, pady=5)
        Button(self.f1, text='返回', command=self.login).grid(row=4, column=1, pady=5)


if __name__ == '__main__':
    root = Tk()
    IyrcUI(root).userMain()
    root.mainloop()
