from Classes.Messaging import Messaging
from Classes.Packets.Server.Socket.KeepAliveServerMessage import KeepAliveServerMessage
from Classes.Packets.PiranhaMessage import PiranhaMessage


class KeepAliveMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self):
        pass

    def decode(self):
        return self

    def execute(message, calling_instance, cryptoInit):
        keepAliveServerMessage = KeepAliveServerMessage(b'')
        Messaging.sendMessage(keepAliveServerMessage, calling_instance.client, cryptoInit)

    def getMessageType(self):
        return 10108

    def getMessageVersion(self):
        return self.messageVersion