import time


class Blog:
    def __init__(self, id, title, author, text='博客内容'):
        self.blogID = id
        self.blogTitle = title
        self.blogAuthor = author
        self.createTime = time.time()
        self.changeTime = time.time()
        self.blogText = text