import grpc
from concurrent import futures
from protos import todo_service_pb2_grpc
from services import todo_service


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    todo_service_pb2_grpc.add_AuthorServicer_to_server(
        todo_service.TodoService(),
        server
    )
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if '__main__' == __name__:
    serve()
