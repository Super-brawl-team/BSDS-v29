from Classes.Packets.PiranhaMessage import PiranhaMessage


class AllianceDataMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0
        self.targetID = []

    def encode(self, calling_instance):
        player = calling_instance.player
        self.writeBoolean(self.targetID == player.AllianceID) # IsOwnAlliance

        self.writeLong(self.targetID[0], self.targetID[1]) # alliance ID
        self.writeString('haccers') # alliance name
        self.writeDataReference(8, 0) # alliance icon
        self.writeVInt(1) # type
        self.writeVInt(1) # member count
        self.writeVInt(9500) # total trophies
        self.writeVInt(0) # minimum trophies to enter
        self.writeVInt(0) # dataref!!!
        self.writeString('CA') # location
        self.writeVInt(1) # people online
        self.writeBoolean(True) # isFamilyFriendly

        self.writeString("this is the hacciest club in the world")

        self.writeVInt(1) # member count
        self.writeLong(0, 2) # player ID
        self.writeVInt(2) # role
        self.writeVInt(9500) # trophies
        self.writeVInt(0) # status: 0=offline 2=online
        self.writeVInt(1) # last connected time seconds ?
        self.writeBoolean(False) # boolean always false?

        self.writeString('risporce') # player name
        self.writeVInt(100) # VInt always 100
        self.writeVInt(28000183) # thumbnail
        self.writeVInt(43000008) # name color


    def decode(self):
        return self

    def execute(message, calling_instance):
        pass

    def getMessageType(self):
        return 24301

    def getMessageVersion(self):
        return self.messageVersion
    
    def setTargetID(self, targetID):
        self.targetID = targetID