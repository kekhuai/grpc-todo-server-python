from protos.todo_service_pb2_grpc import AuthorServicer
from protos.todo_service_pb2 import AuthorResponse


class TodoService(AuthorServicer):
    def GetAuthor(self, request, context):
        return AuthorResponse(id=1, name='test')
