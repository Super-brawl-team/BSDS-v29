from Classes.Packets.PiranhaMessage import PiranhaMessage
from os import urandom


class ServerHelloMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0
        self.sessionKey = None

    def encode(self, fields):
        self.sessionKey = urandom(24)
        self.writeBytes(self.sessionKey, 24)

    def decode(self):
        fields = {}
        fields["Random"] = self.readBytesWithoutLength()
        super().decode(fields)
        return fields

    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 20100

    def getMessageVersion(self):
        return self.messageVersion
    
    def getSessionKey(self):
        return self.sessionKey