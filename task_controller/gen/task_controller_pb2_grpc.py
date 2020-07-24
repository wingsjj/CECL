# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from task_controller.gen import task_controller_pb2 as task__controller_dot_gen_dot_task__controller__pb2


class TaskControllerStub(object):
    """The task controller service definition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AddTask = channel.unary_unary(
                '/TaskController.TaskController/AddTask',
                request_serializer=task__controller_dot_gen_dot_task__controller__pb2.AddTaskReq.SerializeToString,
                response_deserializer=task__controller_dot_gen_dot_task__controller__pb2.AddTaskResp.FromString,
                )
        self.StartTask = channel.unary_unary(
                '/TaskController.TaskController/StartTask',
                request_serializer=task__controller_dot_gen_dot_task__controller__pb2.StartTaskReq.SerializeToString,
                response_deserializer=task__controller_dot_gen_dot_task__controller__pb2.StartTaskResp.FromString,
                )
        self.StopTask = channel.unary_unary(
                '/TaskController.TaskController/StopTask',
                request_serializer=task__controller_dot_gen_dot_task__controller__pb2.StopTaskReq.SerializeToString,
                response_deserializer=task__controller_dot_gen_dot_task__controller__pb2.StopTaskResp.FromString,
                )
        self.FinishTask = channel.unary_unary(
                '/TaskController.TaskController/FinishTask',
                request_serializer=task__controller_dot_gen_dot_task__controller__pb2.FinishTaskReq.SerializeToString,
                response_deserializer=task__controller_dot_gen_dot_task__controller__pb2.FinishTaskResp.FromString,
                )
        self.GetAllTasks = channel.unary_unary(
                '/TaskController.TaskController/GetAllTasks',
                request_serializer=task__controller_dot_gen_dot_task__controller__pb2.GetAllTasksReq.SerializeToString,
                response_deserializer=task__controller_dot_gen_dot_task__controller__pb2.GetAllTasksResp.FromString,
                )
        self.GetTaskInfo = channel.unary_unary(
                '/TaskController.TaskController/GetTaskInfo',
                request_serializer=task__controller_dot_gen_dot_task__controller__pb2.GetTaskInfoReq.SerializeToString,
                response_deserializer=task__controller_dot_gen_dot_task__controller__pb2.GetTaskInfoResp.FromString,
                )
        self.UpdateTask = channel.unary_unary(
                '/TaskController.TaskController/UpdateTask',
                request_serializer=task__controller_dot_gen_dot_task__controller__pb2.UpdateTaskReq.SerializeToString,
                response_deserializer=task__controller_dot_gen_dot_task__controller__pb2.UpdateTaskResp.FromString,
                )
        self.AddCustomLogCallback = channel.unary_unary(
                '/TaskController.TaskController/AddCustomLogCallback',
                request_serializer=task__controller_dot_gen_dot_task__controller__pb2.AddCustomLogCallbackReq.SerializeToString,
                response_deserializer=task__controller_dot_gen_dot_task__controller__pb2.AddCustomLogCallbackResp.FromString,
                )


class TaskControllerServicer(object):
    """The task controller service definition.
    """

    def AddTask(self, request, context):
        """Add a task
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StartTask(self, request, context):
        """Start a task
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StopTask(self, request, context):
        """Stop a task
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FinishTask(self, request, context):
        """It will be called when task finished
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAllTasks(self, request, context):
        """Get all tasks
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTaskInfo(self, request, context):
        """Get task information
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateTask(self, request, context):
        """Update a task
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddCustomLogCallback(self, request, context):
        """Add task script log, will be called by task runtime
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TaskControllerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'AddTask': grpc.unary_unary_rpc_method_handler(
                    servicer.AddTask,
                    request_deserializer=task__controller_dot_gen_dot_task__controller__pb2.AddTaskReq.FromString,
                    response_serializer=task__controller_dot_gen_dot_task__controller__pb2.AddTaskResp.SerializeToString,
            ),
            'StartTask': grpc.unary_unary_rpc_method_handler(
                    servicer.StartTask,
                    request_deserializer=task__controller_dot_gen_dot_task__controller__pb2.StartTaskReq.FromString,
                    response_serializer=task__controller_dot_gen_dot_task__controller__pb2.StartTaskResp.SerializeToString,
            ),
            'StopTask': grpc.unary_unary_rpc_method_handler(
                    servicer.StopTask,
                    request_deserializer=task__controller_dot_gen_dot_task__controller__pb2.StopTaskReq.FromString,
                    response_serializer=task__controller_dot_gen_dot_task__controller__pb2.StopTaskResp.SerializeToString,
            ),
            'FinishTask': grpc.unary_unary_rpc_method_handler(
                    servicer.FinishTask,
                    request_deserializer=task__controller_dot_gen_dot_task__controller__pb2.FinishTaskReq.FromString,
                    response_serializer=task__controller_dot_gen_dot_task__controller__pb2.FinishTaskResp.SerializeToString,
            ),
            'GetAllTasks': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAllTasks,
                    request_deserializer=task__controller_dot_gen_dot_task__controller__pb2.GetAllTasksReq.FromString,
                    response_serializer=task__controller_dot_gen_dot_task__controller__pb2.GetAllTasksResp.SerializeToString,
            ),
            'GetTaskInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTaskInfo,
                    request_deserializer=task__controller_dot_gen_dot_task__controller__pb2.GetTaskInfoReq.FromString,
                    response_serializer=task__controller_dot_gen_dot_task__controller__pb2.GetTaskInfoResp.SerializeToString,
            ),
            'UpdateTask': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateTask,
                    request_deserializer=task__controller_dot_gen_dot_task__controller__pb2.UpdateTaskReq.FromString,
                    response_serializer=task__controller_dot_gen_dot_task__controller__pb2.UpdateTaskResp.SerializeToString,
            ),
            'AddCustomLogCallback': grpc.unary_unary_rpc_method_handler(
                    servicer.AddCustomLogCallback,
                    request_deserializer=task__controller_dot_gen_dot_task__controller__pb2.AddCustomLogCallbackReq.FromString,
                    response_serializer=task__controller_dot_gen_dot_task__controller__pb2.AddCustomLogCallbackResp.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'TaskController.TaskController', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TaskController(object):
    """The task controller service definition.
    """

    @staticmethod
    def AddTask(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/TaskController.TaskController/AddTask',
            task__controller_dot_gen_dot_task__controller__pb2.AddTaskReq.SerializeToString,
            task__controller_dot_gen_dot_task__controller__pb2.AddTaskResp.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StartTask(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/TaskController.TaskController/StartTask',
            task__controller_dot_gen_dot_task__controller__pb2.StartTaskReq.SerializeToString,
            task__controller_dot_gen_dot_task__controller__pb2.StartTaskResp.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StopTask(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/TaskController.TaskController/StopTask',
            task__controller_dot_gen_dot_task__controller__pb2.StopTaskReq.SerializeToString,
            task__controller_dot_gen_dot_task__controller__pb2.StopTaskResp.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def FinishTask(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/TaskController.TaskController/FinishTask',
            task__controller_dot_gen_dot_task__controller__pb2.FinishTaskReq.SerializeToString,
            task__controller_dot_gen_dot_task__controller__pb2.FinishTaskResp.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAllTasks(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/TaskController.TaskController/GetAllTasks',
            task__controller_dot_gen_dot_task__controller__pb2.GetAllTasksReq.SerializeToString,
            task__controller_dot_gen_dot_task__controller__pb2.GetAllTasksResp.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTaskInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/TaskController.TaskController/GetTaskInfo',
            task__controller_dot_gen_dot_task__controller__pb2.GetTaskInfoReq.SerializeToString,
            task__controller_dot_gen_dot_task__controller__pb2.GetTaskInfoResp.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateTask(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/TaskController.TaskController/UpdateTask',
            task__controller_dot_gen_dot_task__controller__pb2.UpdateTaskReq.SerializeToString,
            task__controller_dot_gen_dot_task__controller__pb2.UpdateTaskResp.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddCustomLogCallback(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/TaskController.TaskController/AddCustomLogCallback',
            task__controller_dot_gen_dot_task__controller__pb2.AddCustomLogCallbackReq.SerializeToString,
            task__controller_dot_gen_dot_task__controller__pb2.AddCustomLogCallbackResp.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
