from Classes.Packets.PiranhaMessage import PiranhaMessage

class MatchMakingStatusMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self): 
        self.writeInt(20) # Timer (shows if isProd is disabled)
        self.writeInt(1) # Players Found
        self.writeInt(6) # Max Players
        self.writeInt(0)
        self.writeInt(0)
        self.writeBoolean(True) # show tips
    def decode(self):
        return self

    def execute(message, calling_instance):
        pass

    def getMessageType(self):
        return 20405

    def getMessageVersion(self):
        return self.messageVersion