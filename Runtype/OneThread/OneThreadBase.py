import threading


# 线程类，打开密码文件，自动关闭
class OneThreadBase(threading.Thread):
    def __init__(self, passwordfilepath):
        super().__init__()
        self.path = passwordfilepath  # 密码路径
        self.passfile = open(self.path, "rb")  # 打开文件

    def __del__(self):
        self.passfile.close()

    def run(self):
        pass
