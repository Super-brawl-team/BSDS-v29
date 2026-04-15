from Classes.Packets.PiranhaMessage import PiranhaMessage


class OutOfSyncMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0
        self.serverChecksum = 0
        self.clientChecksum = 0
        self.tick = 0

    def encode(self):
        self.writeVInt(self.serverChecksum)
        self.writeVInt(self.clientChecksum)
        self.writeVInt(self.tick)

    def decode(self):
        self.serverChecksum = self.readVInt()
        self.clientChecksum = self.readVInt()
        self.tick = self.readVInt()
        return self

    def execute(message, calling_instance):
        pass

    def getMessageType(self):
        return 24104

    def getMessageVersion(self):
        return self.messageVersion
    
    def setServerChecksum(self, serverChecksum):
        self.serverChecksum = serverChecksum
        
    def setClientChecksum(self, clientChecksum):
        self.clientChecksum = clientChecksum
        
    def setTick(self, tick):
        self.tick = tick