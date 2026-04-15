from Classes.Packets.PiranhaMessage import PiranhaMessage

class PlayAgainStatusMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self):
        # Play again status 
        self.writeInt(3) # type
        self.writeVInt(0) # team 1 players
        for x in range(0):
            self.writeLong(0, x) # team 1 players id
        self.writeVInt(0) # team 2 players
        for x in range(0):
            self.writeLong(0, x) # team 2 players id
        self.writeInt(1) # huh?
        self.writeInt(1) # huh?
    def decode(self):
        return self

    def execute(message, calling_instance):
        pass

    def getMessageType(self):
        return 24777

    def getMessageVersion(self):
        return self.messageVersion