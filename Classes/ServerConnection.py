import socket
from Database.DatabaseManager import DatabaseManager
import Configuration
from Classes.Connection import Connection
from Classes.Logic.LogicConfiguration import LogicConfiguration

class ServerConnection:
    def __init__(self, address):
        self.config = LogicConfiguration()
        self.db = DatabaseManager()
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if Configuration.settings["DisableNagle"] == True:
            self.server.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, True)
        self.setupConnection(address)

    def setupConnection(self, address):
        self.server.bind(address)
        print("Listening for new connection...")
        while True:
            self.server.listen()
            socket, address = self.server.accept()
            print("New connection with address", address[0], "on port", address[1])
            Connection(self, socket, address).start()