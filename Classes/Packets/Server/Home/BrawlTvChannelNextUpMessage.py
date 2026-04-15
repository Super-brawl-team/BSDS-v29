from Classes.Packets.PiranhaMessage import PiranhaMessage

class BrawlTvChannelNextUpMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self):
        self.writeVInt(1) # IDK
        self.writeVInt(0) # uuh
        self.writeBoolean(True)
        if True:
            self.writeLong(0,1)
        self.writeStringReference("hacc1") # selected channel?
        
    def decode(self):
        
        return self
    
    def execute(message, calling_instance):
        pass

    def getMessageType(self):
        return 24701

    def getMessageVersion(self):
        return self.messageVersion
