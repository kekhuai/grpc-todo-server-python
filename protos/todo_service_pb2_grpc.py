# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from protos import todo_service_pb2 as protos_dot_todo__service__pb2


class AuthorStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetAuthor = channel.unary_unary(
        '/todo.Author/GetAuthor',
        request_serializer=protos_dot_todo__service__pb2.AuthorRequest.SerializeToString,
        response_deserializer=protos_dot_todo__service__pb2.AuthorResponse.FromString,
        )


class AuthorServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetAuthor(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_AuthorServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetAuthor': grpc.unary_unary_rpc_method_handler(
          servicer.GetAuthor,
          request_deserializer=protos_dot_todo__service__pb2.AuthorRequest.FromString,
          response_serializer=protos_dot_todo__service__pb2.AuthorResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'todo.Author', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))