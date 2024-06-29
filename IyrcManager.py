from hvplot import ui

import IyrcDB
from tkinter import *
from tkinter import messagebox

import User


class IyrcManager:
    def __init__(self):
        self.db = IyrcDB.IyrcDB()
        self.user = User.User(-1, 'test', '临时', 'test@临时')
        self.blogid = 0

    def login(self, ui):
        # 输入正确性验证
        username = ui.username.get()
        password = ui.password.get()
        print('login')

        self.db.open()
        user, msg = self.db.checkPassword(username, password)
        self.db.close()
        if user is not None:
            self.user = user
            if user.type == 'ADMIN':
                ui.adminMain()
            else:
                ui.userMain()

        ui.message.delete(0, END)
        ui.message.insert(END, msg)

    def register(self, ui):
        # 输入正确性验证
        username = ui.username.get()
        password = ui.password.get()
        password2 = ui.password2.get()
        email = ui.email.get()

        if password != password2:
            ui.message.delete(0, END)
            ui.message.insert(END, '两次密码不一致')
            return

        self.db.open()
        if self.db.userExist(username):
            ui.message.delete(0, END)
            ui.message.insert(END, '用户名已存在')
            self.db.close()
            return
        else:
            self.db.insertUser(username, password, email, 'USER')
        if self.db.userExist(username):
            ui.message.delete(0, END)
            ui.message.insert(END, '注册成功')
        self.db.close()

    def selectBlog(self, ui):
        self.db.open()
        r = self.db.selectBlog(ui.blogID.get())
        self.db.close()
        if r is not None:
            self.blogid = r[0]
            ui.toSelectBlog()
            ui.blogid.delete(0, END)
            ui.blogid.insert(END, str(r[0]))
            ui.blogtitle.delete(0, END)
            ui.blogtitle.insert(END, r[1])
            ui.author.delete(0, END)
            ui.author.insert(END, r[2])
            ui.blogcreatetime.delete(0, END)
            ui.blogcreatetime.insert(END, r[3])
            ui.blogupdatetime.delete(0, END)
            ui.blogupdatetime.insert(END, r[4])
            ui.blogtext.delete(1.0, END)
            ui.blogtext.insert(END, r[5])
            ui.message.delete(0, END)
            ui.message.insert(END, '查找成功')
            if self.user.userName == r[2]:
                Button(ui.f2, text='修改', command=lambda: self.updateBlog(ui)).grid(row=7, column=1, pady=5)
                Button(ui.f2, text='删除', command=lambda: self.deleteBlog(ui)).grid(row=7, column=2, pady=5)
        else:
            ui.blogid.delete(0, END)
            ui.blogtitle.delete(0, END)
            ui.author.delete(0, END)
            ui.blogcreatetime.delete(0, END)
            ui.blogupdatetime.delete(0, END)
            ui.blogtext.delete(1.0, END)
            ui.message.delete(0, END)
            ui.message.insert(END, '查找失败，请检查输入')

    def updateBlog(self, ui):
        self.db.open()
        self.db.updateBlog(ui.blogtitle.get(), ui.blogtext.get(1.0, END), self.blogid)
        self.db.close()
        ui.message.delete(0, END)
        ui.message.insert(END, '修改成功')
        self.selectMyBlog(ui)

    def deleteBlog(self, ui):
        self.db.open()
        self.db.deleteBlog(self.blogid)
        self.db.close()
        ui.message.delete(0, END)
        ui.message.insert(END, '删除成功')
        self.selectMyBlog(ui)

    def selectMyBlog(self, ui):
        ui.toMyBlog()
        self.db.open()
        r = self.db.selectMyBlog(self.user.userName)
        if r is not None:
            for i in r:
                ui.tree.insert("", i[0], text=str(i[0]), values=(i[1], i[2], i[3], i[4]))
            ui.tree.pack()
        else:
            ui.message.delete(0, END)
            ui.message.insert(END, '你没有博客')
        self.db.close()

    def insertBlog(self, ui):
        self.db.open()
        self.db.insertBlog(ui.blogtitle.get(), self.user.userName, ui.blogtext.get(1.0, END))
        self.db.close()
        ui.message.delete(0, END)
        ui.message.insert(END, '创建博客成功')
        self.selectMyBlog(ui)

    def showUserInfo(self, ui):
        # 输入正确性验证
        ui.username.delete(0, END)
        ui.username.insert(END, self.user.userName)
        ui.password.delete(0, END)
        ui.password.insert(END, self.user.password)
        ui.email.delete(0, END)
        ui.email.insert(END, self.user.email)
        ui.type.delete(0, END)
        ui.type.insert(END, self.user.type)
        ui.message.delete(0, END)
        ui.message.insert(END, '修改后请点击按钮')

    def updateUserInfo(self, ui):
        self.db.open()
        self.db.updateUser(ui.username.get(), ui.password.get(), ui.email.get(), self.user.userID)
        self.db.close()
        self.user.userName = ui.username.get()
        self.user.userPassword = ui.password.get()
        self.user.email = ui.email.get()
        ui.message.delete(0, END)
        ui.message.insert(END, '修改完成')

    def selectMyBook(self, ui):
        ui.toMyBook()
        self.db.open()
        r = self.db.selectMyBook(self.user.userID)
        if r is not None:
            for i in r:
                j = self.db.selectBook(int(i[1]))
                ui.tree.insert("", str(j[0]), text=str(j[0]), values=(j[1], j[2]))
            ui.tree.pack()
        else:
            ui.message.delete(0, END)
            ui.message.insert(END, '没有书籍')
        self.db.close()

    def selectBook(self, ui):
        pass

    def insertBook(self, ui):
        pass

    def insertMyBook(self, ui):
        self.db.open()
        self.db.insertMyBook(self.user.userID, ui.bookID.get())
        self.db.close()
        ui.message.delete(0, END)
        ui.message.insert(END, '添加成功')
        self.selectMyBook(ui)

    def updateBook(self, ui):
        pass

    def deleteBook(self, ui):
        pass

    def deleteMyBook(self, ui):
        self.db.open()
        self.db.deleteMyBook(self.user.userID, ui.bookID.get())
        self.db.close()
        ui.message.delete(0, END)
        ui.message.insert(END, '删除成功')
        self.selectMyBook(ui)
