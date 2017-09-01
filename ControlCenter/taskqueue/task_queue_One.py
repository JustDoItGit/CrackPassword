import ControlCenter.taskqueue.taskqueue_base
import ControlCenter.task.task


class taskQueue_One(ControlCenter.taskqueue.taskqueue_base.taskQueue_base):
    def __init__(self, queue):
        super().__init__(queue)

    def run(self):
        while True:
            mylist = self.queue.get()
            print(mylist)
            mytask = ControlCenter.task.task.Task(mylist[0], mylist[1])
            mytask.start()  # 开启
            mytask.join()
