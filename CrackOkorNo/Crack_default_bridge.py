import CrackOkorNo.Database.Crack_Mysql


class Crack_deafult_Bridage:  # 桥接，默认值
    def __new__(self, password, databasetype):
        if databasetype == "mysql":
            return CrackOkorNo.Database.Crack_Mysql.Crack_mysql("root",
                                                                password,
                                                                "127.0.0.1",
                                                                "3306",
                                                                "xiaomi"
                                                                )
        else:
            return None


'''
t=  Crack_deafult_Bridage("111111","mysql")
print(type(t))
print(t.password)
print(t.user)
print(t.port)
'''
