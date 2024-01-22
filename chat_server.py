import grpc
from concurrent import futures
import threading
import time

import chat_pb2
import chat_pb2_grpc

class ChatServer(chat_pb2_grpc.ChatServicer):
    def __init__(self):
        self.messages = []
        self.lock = threading.Lock()

    def SendMessage(self, request, context):
        with self.lock:
            self.messages.append(request)
        return chat_pb2.Empty()

    def ReceiveMessage(self, request, context):
        while True:
            with self.lock:
                for message in self.messages:
                    yield message
                self.messages = []
            time.sleep(1)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    chat_pb2_grpc.add_ChatServicer_to_server(ChatServer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(3600)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
