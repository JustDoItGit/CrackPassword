import ControlCenter.cmd.cmd
import ControlCenter.task.task
import ControlCenter.taskqueue.task_queue_One  # 任务队列
import queue

if __name__ == "__main__":
    queue = queue.Queue(10)  # 任务队列最大容量为10

    path = "密码字典路径"  # 参数
    mycmd = ControlCenter.cmd.cmd.CMD("mysql", 1)

    mytaskqueue = ControlCenter.taskqueue.task_queue_One.taskQueue_One(queue)  # 开启任务队列
    mytaskqueue.start()  # 队列开始执行
    mytaskqueue.addtask([path, mycmd])  # 增加任务

'''
if  __name__=="__main__":
    print("程序开始")


    #addtask([path,mycmd])


    print("完成")

'''
