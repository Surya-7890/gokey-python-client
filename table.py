import socket as Socket
import json

class Table:
    name: str
    socket: Socket.socket

    def __init__(self, name: str, socket: Socket.socket) -> None:
        self.name = name
        self.socket = socket
    
    def set(self, key: str, val: str):
        try:
            self.socket.send(bytes(f"SET {key} {val} {self.name}", "utf-8"))
            response = ""
            while True:
                data = self.socket.recv(1024)
                data = str(data.decode("utf-8"))
                response += data
                if response.endswith("\n"):
                    response = response.strip("\n")
                    break
            return response
        except Socket.error as e:
            return f"socket error: {e}"
        except Exception as e:
            return f"exception: {e}"
    
    def setEX(self, key: str, val: str, expiry: int):
        try:
            self.socket.send(bytes(f"SETEX {key} {val} {self.name} {expiry}", "utf-8"))
            response = b""
            while True:
                data = self.socket.recv(1024)
                response += data
                if response.endswith("\n") or not data:
                    response = response.strip("\n")
                    break
            json_data = json.loads(response)
            return json_data
        except Socket.error as e:
            return f"socket error: {e}"
        except Exception as e:
            return f"exception: {e}"

    def delete(self, key: str) -> str:
        try:
            self.socket.send(bytes(f"DELETE {key} {self.name}", "utf-8"))
            response = ""
            while True:
                data = self.socket.recv(1024)
                data = str(data.decode("utf-8"))
                response += data
                if response.endswith("\n"):
                    response = response.strip("\n")
                    break
            return data
        except Socket.error as e:
            return f"socket error: {e}"
        except Exception as e:
            return f"exception: {e}"

    def get(self, key: str) -> str:
        try:
            self.socket.send(bytes(f"GET {key} {self.name}", "utf-8"))
            response = ""
            while True:
                data = self.socket.recv(1024)
                data = str(data.decode("utf-8"))
                response += data
                if response.endswith("\n"):
                    response = response.strip("\n")
                    break
            return data
        except Socket.error as e:
            return f"socket error: {e}"
        except Exception as e:
            return f"exception: {e}"

    def getAll(self) -> dict:
        try:
            self.socket.send(bytes(f"GET * {self.name}", "utf-8"))
            response = ""
            while True:
                data = self.socket.recv(1024)
                data = str(data.decode("utf-8"))
                response += data
                if response.endswith("\n"):
                    response = response.strip("\n")
                    break
            return data
        except Socket.error as e:
            return f"socket error: {e}"
        except Exception as e:
            return f"exception: {e}"
