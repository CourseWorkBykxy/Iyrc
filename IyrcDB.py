import sqlite3
import time

from User import User
from Blog import Blog


class IyrcDB:
    dbName = 'Iyrc.db'

    def __init__(self):
        self.open()
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS USER
               (ID INT PRIMARY KEY     NOT NULL,
               USERNAME        TEXT    NOT NULL,
               PASSWORD          TEXT    NOT NULL,
               EMAIL           TEXT,
               TYPE            TEXT    NOT NULL);''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS BOOK
                       (ID INT PRIMARY KEY     NOT NULL,
                       NAME           TEXT    NOT NULL,
                       AUTHOR         TEXT    NOT NULL,
                       TEXT           TEXT);''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS BLOG
                       (ID INT PRIMARY KEY     NOT NULL,
                       TITLE           TEXT    NOT NULL,
                       AUTHOR          TEXT    NOT NULL,
                       CREATE_TIME     INT     NOT NULL,
                       CHANGE_TIME     INT     NOT NULL,
                       TEXT            TEXT);''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS USERBOOK
                               (USERID TEXT     NOT NULL,
                               BOOKID  TEXT    NOT NULL);''')
        self.conn.commit()
        self.conn.close()

    def open(self):
        self.conn = sqlite3.connect(self.dbName)

    def close(self):
        self.conn.close()

    '''
    sql使用？作为占位符
    values类型为元组
    values为空则正常执行sql
    '''

    def runSQL(self, sql, values=None):

        cursor = self.conn.cursor()
        if values is None:
            try:
                cursor.execute(sql)
                self.conn.commit()

            except IOError as e:
                print(e)
        else:
            try:
                cursor.execute(sql, values)
                self.conn.commit()
            except IOError as e:
                print(e)
        return cursor

    '''
    用户存在性验证，
    输入
    username str 用户名
    '''

    def userExist(self, username):
        sql = 'select COUNT(USERNAME) from USER where USERNAME = ?'
        cursor = self.runSQL(sql, (username,))
        r = cursor.fetchone()[0]
        if r == 0:
            return False
        else:
            return True

    '''
    测试密码
    输入
    用户名
    密码
    '''

    def checkPassword(self, username, password):
        sql = 'select * from USER where USERNAME = ?'
        cursor = self.runSQL(sql, (username,))
        r = cursor.fetchone()
        if r is None:
            return None, '用户名不存在'
        elif r[2] != password:
            return None, '密码错误'
        else:
            return User(r[0], r[1], r[2], r[3], r[4]), '验证成功'

    '''
    获取可用ID
    '''

    def getID(self, tableName):
        sql = 'select MAX(ID) from {}'.format(tableName)
        cursor = self.runSQL(sql)
        r = cursor.fetchone()[0]
        if r is None:
            return 0
        else:
            return r + 1

    '''
    插入初始内容
    '''

    def DBInit(self):
        if not self.userExist('admin'):
            self.insertUser('admin', 'admin', '@', 'ADMIN')
        for i in range(5):
            username = 'USER' + str(i)
            if not self.userExist(username):
                self.insertUser(username, '123', '@', 'USER')

    '''
    插入用户
    '''

    def insertUser(self, username, password, email, type):
        sql = 'insert into USER(ID,USERNAME,PASSWORD,EMAIL,TYPE) values(?,?,?,?,?)'
        self.runSQL(sql, (self.getID('USER'), username, password, email, type,))

    def updateUser(self, username, password, email, id):
        sql = 'update USER set USERNAME=?,PASSWORD=?,EMAIL=? where ID=?'
        self.runSQL(sql, (username, password, email, id,))

    def insertBlog(self, title, author, text):
        sql = 'insert into BLOG(ID,TITLE,AUTHOR,CREATE_TIME,CHANGE_TIME,TEXT) values(?,?,?,?,?,?)'
        self.runSQL(sql, (self.getID('BLOG'), title, author,
                          time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                          time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), text,))

    def updateBlog(self, title, text, id):
        sql = 'update BLOG set TITLE=?,CHANGE_TIME=?,TEXT=? where ID=?'
        self.runSQL(sql, (title, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), text, id,))

    def deleteBlog(self, id):
        sql = 'delete from BLOG where ID=?'
        self.runSQL(sql, (id,))

    def selectAllBlog(self):
        sql = 'select * from BLOG'
        return self.runSQL(sql)

    def selectBlog(self, id):
        sql = 'select * from BLOG where ID=?'
        cursor = self.runSQL(sql, (id,))
        return cursor.fetchone()

    def selectMyBlog(self, id):
        sql = 'select * from BLOG where AUTHOR=?'
        return self.runSQL(sql, (id,))

    def insertMyBook(self, userid, bookid):
        sql = 'insert into USERBOOK(USERID,BOOKID) values(?,?)'
        self.runSQL(sql, (userid, bookid,))

    def insertBook(self, title, author, text):
        sql = 'insert into BOOK(ID,NAME,AUTHOR,TEXT) values(?,?,?,?)'
        self.runSQL(sql, (self.getID('BOOK'), title, author, text,))

    def updateBook(self, title, author, text, id):
        sql = 'update BOOK set NAME=?,AUTHOR=?,TEXT=? where ID=?'
        self.runSQL(sql, (title, author, text, id,))

    def deleteMyBook(self, userid, bookid):
        sql = 'delete from USERBOOK where USERID=? AND BOOKID=?'
        self.runSQL(sql, (userid,bookid,))

    def deleteBook(self, id):
        sql = 'delete from BOOK where ID=?'
        self.runSQL(sql, (id,))

    def selectAllBook(self):
        sql = 'select * from BOOK'
        return self.runSQL(sql)

    def selectBook(self, id):
        sql = 'select * from BOOK where ID=?'
        cursor = self.runSQL(sql, (id,))
        return cursor.fetchone()

    def selectMyBook(self, id):
        sql = 'select * from USERBOOK where USERID=?'
        return self.runSQL(sql, (id,))

# db = IyrcDB()
# db.open()
# db.DBInit()
#
# print(db.selectBlog(1))
# db.close()
