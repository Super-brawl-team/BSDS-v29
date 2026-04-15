from Classes.Packets.PiranhaMessage import PiranhaMessage


class KeepAliveServerMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self):
        pass

    def decode(self):
        return self

    def execute(message, calling_instance):
        pass

    def getMessageType(self):
        return 20108

    def getMessageVersion(self):
        return self.messageVersion