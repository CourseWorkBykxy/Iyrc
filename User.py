class User:
    def __init__(self, id, name, password, email, type='USER'):
        self.userID = id
        self.userName = name
        self.password = password
        self.email = email
        self.type = type
