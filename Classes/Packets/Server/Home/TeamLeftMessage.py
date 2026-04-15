from Classes.Packets.PiranhaMessage import PiranhaMessage


class TeamLeftMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0
        self.reason = 0

    def encode(self, calling_instance):
        self.writeInt(self.reason)

    def decode(self):
        self.reason = self.readInt()
        return self

    def execute(message, calling_instance):
        pass

    def getMessageType(self):
        return 24125

    def getMessageVersion(self):
        return self.messageVersion
    
    def setReason(self, reason):
        self.reason = reason