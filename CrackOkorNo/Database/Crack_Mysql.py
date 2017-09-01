import CrackOkorNo.Database.Crack_Bigdatabase
import pymysql


class Crack_mysql(CrackOkorNo.Database.Crack_Bigdatabase.Crack_Bigdatabase):
    def __init__(self, user, password, ip, port, database):
        super().__init__(user, password, ip, port, database)

    def CrackPassword(self, **arg):  # 接口，返回True,返回False
        try:
            tryconnect = pymysql.connect(self.ip, self.user, self.password, self.database)
            print(tryconnect)
            tryconnect.close()
            return True
        except:
            return False


'''
# 测试
t1 = Crack_mysql("root", "111111", "127.0.0.1", "3306", "xiaomi")
print(t1.CrackPassword())
'''
