from Classes.Packets.PiranhaMessage import PiranhaMessage
from os import urandom


class ServerHelloMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0
        self.sessionKey = None

    def encode(self):
        self.sessionKey = urandom(24)
        self.writeBytes(self.sessionKey, 24)

    def decode(self):
        self.sessionKey = self.readBytesWithoutLength()
        return self

    def execute(message, calling_instance):
        pass

    def getMessageType(self):
        return 20100

    def getMessageVersion(self):
        return self.messageVersion
    
    def getSessionKey(self):
        return self.sessionKey