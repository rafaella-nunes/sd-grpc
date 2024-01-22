import grpc
import threading
import time

import chat_pb2
import chat_pb2_grpc

class ChatClient:
    def __init__(self, user):
        self.user = user
        self.channel = grpc.insecure_channel('localhost:50051')
        self.stub = chat_pb2_grpc.ChatStub(self.channel)

    def send_messages(self):
        while True:
            content = input("Enter your message: \n")
            message = chat_pb2.Message(user=self.user, content=content)
            self.stub.SendMessage(message)
            time.sleep(1)

    def receive_messages(self):
        for message in self.stub.ReceiveMessage(chat_pb2.Empty()):
            print(f"{message.user}: {message.content}")

def main():
    user = input("Enter your username: \n")
    client = ChatClient(user)

    send_thread = threading.Thread(target=client.send_messages)
    receive_thread = threading.Thread(target=client.receive_messages)

    send_thread.start()
    receive_thread.start()

    send_thread.join()
    receive_thread.join()

if __name__ == '__main__':
    main()
