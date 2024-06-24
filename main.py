import socket as Socket
from table import Table

s = Socket.socket()

class Client:
    socket: Socket.socket
    host: str
    port: int

    def __init__(self, host: str, port: int) -> None:
        self.host = host
        self.port = port
        s = Socket.socket(Socket.AF_INET, Socket.SOCK_STREAM)
        self.socket = s

    def connect(self) -> str | None:
        try:
            self.socket.connect((self.host, self.port))
        except:
            return "error while connecting"

    def disconnect(self) -> None:
        self.socket.close()

    def create_table(self, name: str) -> Table:
        try:
            self.socket.send(bytes(f"CREATE {name}", "utf-8"))
            response = ""
            while True:
                data = self.socket.recv(1024)
                data = str(data.decode("utf-8"))
                response += data
                if (response.endswith("\n")):
                    response = response.strip("\n")
                    break   
            return Table(name=name, socket=self.socket)
        except Socket.error as e:
            return f"socket error: {e}"
        except Exception as e:
            return f"exception: {e}"