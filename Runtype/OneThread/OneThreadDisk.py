import Runtype.OneThread.OneThreadBase
import CrackOkorNo.Crack_default_bridge


class OneThreadDisk(Runtype.OneThread.OneThreadBase.OneThreadBase):
    def __init__(self, passwordpath, cracktype):
        super().__init__(passwordpath)
        self.cracktype = cracktype

    def run(self):
        while True:
            linedata = self.passfile.readline()  # 读取一行
            if not linedata:  # 读取完成跳出
                break
            linedata = linedata.decode("gbk", "ignore")
            linelist = linedata.split(" # ")
            # print(linelist[0])#密码
            mysql = CrackOkorNo.Crack_default_bridge.Crack_deafult_Bridage(linelist[0], self.cracktype)
            isOK = mysql.CrackPassword()  # 测试成功失败
            print(mysql.password, isOK)
            if isOK:
                break


'''
path="密码字典路径"
one=OneThreadDisk(path)
one.start()
'''
