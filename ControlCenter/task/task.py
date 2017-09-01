import threading
import ControlCenter.cmd.cmd  # 命令
import Runtype.OneThread.OneThreadDisk


class Task(threading.Thread):
    def __init__(self, path, goCMD):
        super().__init__()
        self.goCMD = goCMD  # 命令与路径
        self.path = path

    def run(self):  # 开启线程
        if self.goCMD.cmd == "mysql":
            print("task is  run ")
            one = Runtype.OneThread.OneThreadDisk.OneThreadDisk(self.path, self.goCMD.cmd)
            one.start()
            one.join()
