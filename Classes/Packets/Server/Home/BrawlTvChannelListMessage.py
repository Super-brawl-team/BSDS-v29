from Classes.Packets.PiranhaMessage import PiranhaMessage

class BrawlTvChannelListMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self):
        self.writeVInt(1) # count
        for x in range(1):
            self.writeVInt(1)
            self.writeStringReference("hacc")
            self.writeStringReference("hacc2")
        
    def decode(self):
        
        return self
    
    def execute(message, calling_instance):
        pass

    def getMessageType(self):
        return 24700

    def getMessageVersion(self):
        return self.messageVersion
