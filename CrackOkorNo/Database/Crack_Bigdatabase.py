import CrackOkorNo.Crack_base

class Crack_Bigdatabase(CrackOkorNo.Crack_base.Crack_base):
    def __init__(self, user, password, ip, port, database):
        super().__init__()
        self.user = user
        self.password = password
        self.ip = ip
        self.port = port
        self.database = database
