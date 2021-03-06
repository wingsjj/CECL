from concurrent import futures
import time
import data_manager.dal.task
import json
from data_manager.model.task import Task
from data_manager.model.custom_log import CustomLog
from conf import DATA_MANAGER_SERVER

import grpc

from data_manager.gen import data_manager_pb2, data_manager_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class DataManager(data_manager_pb2_grpc.DataManagerServicer):

    def __init__(self):
        self.db = data_manager.dal.task.Db()

    def AddTask(self, request, context):
        print(request.task)
        # status:0 -> ready
        t: Task = request.task
        task_id = self.db.add_task(Task(
            t.task_id,
            t.name,
            t.create_time,
            t.start_time,
            t.end_time,
            t.union_train,
            t.edgenodes,
            t.file,
            0,
        ))
        return data_manager_pb2.AddTaskResp(resp=data_manager_pb2.Response(code=0, message=json.dumps(task_id)))

    def StartTask(self, request, context):
        print("start task:" + str(request.task_id))
        print("time:" + str(request.start_time))
        self.db.start_task(Task(
            task_id=request.task_id,
            start_time=request.start_time,
        ))
        return data_manager_pb2.StartTaskResp(resp=data_manager_pb2.Response(code=0, message="success"))

    def StopTask(self, request, context):
        self.db.stop_task(Task(
            task_id=request.task_id,
            end_time=request.stop_time,
        ))
        return data_manager_pb2.StopTaskResp(resp=data_manager_pb2.Response(code=0, message="success"))

    def FinishTask(self, request, context):
        print("finish task")
        self.db.finish_task(Task(
            task_id=request.task_id,
            end_time=request.finish_time,
        ))
        return data_manager_pb2.FinishTaskResp(resp=data_manager_pb2.Response(code=0, message="success"))

    def GetTask(self, request, context):
        t: Task = request.task
        return data_manager_pb2.GetTaskResp(
            resp=data_manager_pb2.Response(code=0, message=json.dumps(self.db.get_task(t.task_id))))

    def GetAllTasks(self, request, context):
        print(self.db.get_all_tasks())
        return data_manager_pb2.GetAllTasksResp(
            resp=data_manager_pb2.Response(code=0, message=json.dumps(self.db.get_all_tasks())))

    def UpdateTask(self, request, context):
        t: Task = request.task
        self.db.update_task(Task(
            t.task_id,
            t.name,
            t.create_time,
            t.start_time,
            t.end_time,
            t.union_train,
            t.edgenodes,
            t.file,
            t.status,
        ))
        return data_manager_pb2.UpdateTaskResp(resp=data_manager_pb2.Response(code=0, message="success"))

    def AddCustomLog(self, request, context):
        t: CustomLog = request.custom_log
        if t.task_id == 0:
            return data_manager_pb2.AddCustomLogResp(
                resp=data_manager_pb2.Response(code=10001, message="task id can't be zero"))
        if t.content == '':
            return data_manager_pb2.AddCustomLogResp(
                resp=data_manager_pb2.Response(code=10001, message="content can't be empty"))
        if time == 0:
            return data_manager_pb2.AddCustomLogResp(
                resp=data_manager_pb2.Response(code=10001, message="time can't be zero"))
        self.db.add_custom_log(CustomLog(
            t.task_id,
            t.content,
            t.time
        ))
        return data_manager_pb2.AddCustomLogResp(resp=data_manager_pb2.Response(code=0, message="success"))

    def GetTaskLog(self, request, context):
        return data_manager_pb2.GetAllTasksResp(
            resp=data_manager_pb2.Response(code=0, message=json.dumps(self.db.get_task_log(request.task_id))))

    # # 工作函数
    # def SayHello(self, request, context):
    #     print(request)
    #     date_array = datetime.datetime.utcfromtimestamp(request.date)
    #     other_style_time = date_array.strftime("%Y-%m-%d %H:%M:%S")
    #     print(other_style_time)
    #     return hello_pb2.HelloReply(message='Hello, %s!' % request.name, date=other_style_time)


def serve():
    # gRPC 服务器
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=6))
    data_manager_pb2_grpc.add_DataManagerServicer_to_server(DataManager(), server)
    server.add_insecure_port(DATA_MANAGER_SERVER)
    server.start()  # start() 不会阻塞，如果运行时你的代码没有其它的事情可做，你可能需要循环等待。
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
