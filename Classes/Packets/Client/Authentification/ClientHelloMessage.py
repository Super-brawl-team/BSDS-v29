from Classes.Messaging import Messaging
from Classes.Packets.Server.Authentification.ServerHelloMessage import ServerHelloMessage
from Classes.Packets.PiranhaMessage import PiranhaMessage


class ClientHelloMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self):
        pass

    def decode(self):
        self.readInt() # protocol
        self.readInt() # key version
        self.readInt() # major version
        self.readInt() # minor version
        self.readInt() # build
        self.readString()  # content hash
        self.readInt() # device type
        self.readInt() # appstore
        return self

    def execute(message, calling_instance, cryptoInit):
        serverHelloMessage = ServerHelloMessage(b'')
        Messaging.sendMessage(serverHelloMessage, calling_instance.client, cryptoInit)

    def getMessageType(self):
        return 10100

    def getMessageVersion(self):
        return self.messageVersion