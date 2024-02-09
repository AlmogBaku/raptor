# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from py_runtime.v1alpha1 import api_pb2 as py__runtime_dot_v1alpha1_dot_api__pb2


class RuntimeServiceStub(object):
    """RuntimeService is the service that exposes the runtime API. This is usually used by Raptor developers or advanced users.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.LoadProgram = channel.unary_unary(
                '/py_runtime.v1alpha1.RuntimeService/LoadProgram',
                request_serializer=py__runtime_dot_v1alpha1_dot_api__pb2.LoadProgramRequest.SerializeToString,
                response_deserializer=py__runtime_dot_v1alpha1_dot_api__pb2.LoadProgramResponse.FromString,
                )
        self.ExecuteProgram = channel.unary_unary(
                '/py_runtime.v1alpha1.RuntimeService/ExecuteProgram',
                request_serializer=py__runtime_dot_v1alpha1_dot_api__pb2.ExecuteProgramRequest.SerializeToString,
                response_deserializer=py__runtime_dot_v1alpha1_dot_api__pb2.ExecuteProgramResponse.FromString,
                )


class RuntimeServiceServicer(object):
    """RuntimeService is the service that exposes the runtime API. This is usually used by Raptor developers or advanced users.
    """

    def LoadProgram(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ExecuteProgram(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RuntimeServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'LoadProgram': grpc.unary_unary_rpc_method_handler(
                    servicer.LoadProgram,
                    request_deserializer=py__runtime_dot_v1alpha1_dot_api__pb2.LoadProgramRequest.FromString,
                    response_serializer=py__runtime_dot_v1alpha1_dot_api__pb2.LoadProgramResponse.SerializeToString,
            ),
            'ExecuteProgram': grpc.unary_unary_rpc_method_handler(
                    servicer.ExecuteProgram,
                    request_deserializer=py__runtime_dot_v1alpha1_dot_api__pb2.ExecuteProgramRequest.FromString,
                    response_serializer=py__runtime_dot_v1alpha1_dot_api__pb2.ExecuteProgramResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'py_runtime.v1alpha1.RuntimeService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class RuntimeService(object):
    """RuntimeService is the service that exposes the runtime API. This is usually used by Raptor developers or advanced users.
    """

    @staticmethod
    def LoadProgram(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/py_runtime.v1alpha1.RuntimeService/LoadProgram',
            py__runtime_dot_v1alpha1_dot_api__pb2.LoadProgramRequest.SerializeToString,
            py__runtime_dot_v1alpha1_dot_api__pb2.LoadProgramResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ExecuteProgram(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/py_runtime.v1alpha1.RuntimeService/ExecuteProgram',
            py__runtime_dot_v1alpha1_dot_api__pb2.ExecuteProgramRequest.SerializeToString,
            py__runtime_dot_v1alpha1_dot_api__pb2.ExecuteProgramResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
