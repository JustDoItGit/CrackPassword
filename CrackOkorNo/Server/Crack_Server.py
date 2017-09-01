import CrackOkorNo.Crack_base
import error.exception.abstract

class Crack_Server(CrackOkorNo.Crack_base.Crack_base):
    def __init__(self, ip, port, user, password):
        print(self.__class__)
        if self.__class__ is Crack_Server:  # 判断类型是否自身，是的触发异常
            raise error.exception.abstract.Abstract()  # raise引发一个异常 异常类型
        super().__init__()
        self.ip = ip
        self.port = port
        self.user = user
        self.password = password

        def CrackPassword(self):  # return true or false
            pass

'''
## 测试raise引发异常
host="47.93.29.25"
user="root"
password="Admin123"
port=22
myftp=Crack_Server(host,port,user,password)
print(myftp.password)
'''