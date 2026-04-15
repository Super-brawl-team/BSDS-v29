from Classes.Packets.PiranhaMessage import PiranhaMessage


class LoginFailedMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0
        self.errorID = 0
        self.fingerprintData = "{}"
        self.contentURL = ""
        self.updateURl = ""
        self.reason = ""

    def encode(self):
        self.writeInt(self.errorID)
        self.writeString(self.fingerprintData)
        self.writeString()
        self.writeString(self.contentURL)
        self.writeString(self.updateURl)
        self.writeString(self.reason)
        self.writeInt(0)
        self.writeBoolean(False)
        self.writeInt(0)
        self.writeInt(0)
        self.writeInt(0)
        self.writeInt(0)
        self.writeString()
        self.writeInt(0)
        self.writeBoolean(True)
        self.writeBoolean(True)
        self.writeString()
        self.writeVInt(0)
        self.writeString()
        self.writeBoolean(False)

    def decode(self):
        self.errorID = self.readInt()
        self.fingerprintData = self.readString()
        self.readString() #RedirectDomain
        self.contentURL = self.readString()
        self.updateURl = self.readString()
        self.reason = self.readString()
        return self

    def execute(message, calling_instance):
        pass

    def getMessageType(self):
        return 20103

    def getMessageVersion(self):
        return self.messageVersion
    
    def setErrorID(self, ID):
        self.errorID = ID
        
    def setFingerprintData(self, fingerprintData):
        self.fingerprintData = fingerprintData
    
    def setContentURL(self, contentURL):
        self.contentURL = contentURL
    
    def setReason(self, reason):
        self.reason = reason
        
    def setUpdateURL(self, updateURl):
        self.updateURl = updateURl