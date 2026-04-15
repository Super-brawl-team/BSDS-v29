from Classes.Packets.PiranhaMessage import PiranhaMessage
from Classes.Entries.PlayerDisplayData import PlayerDisplayData

class PlayerProfileMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0
        self.targetID = []

    def encode(self, calling_instance):
        db = calling_instance.db
        player = db.loadInstance(db.getTokenByLowId(self.targetID[1]))
        self.writeLogicLong(self.targetID)
        self.writeDataReference(0)
        self.writeVInt(len(player.OwnedBrawlers))
        for i,x in player.OwnedBrawlers.items():
            self.writeDataReference(16, i)
            self.writeDataReference(0)
            self.writeVInt(x["Trophies"]) # trophies
            self.writeVInt(x["HighestTrophies"]) # highestTrophies
            self.writeVInt(x["PowerLevel"]) #power level
        
        self.writeVInt(12)

        self.writeVInt(1) 
        self.writeVInt(1) # 3v3 victories

        self.writeVInt(2)
        self.writeVInt(player.Experience) # total exp

        self.writeVInt(3)
        self.writeVInt(player.Trophies) # current trophies

        self.writeVInt(4)
        self.writeVInt(player.HighestTrophies) # highest trophies

        self.writeVInt(5) 
        self.writeVInt(len(player.OwnedBrawlers)) # unlocked brawlers

        self.writeVInt(8)
        self.writeVInt(6) # solo victories

        self.writeVInt(11) 
        self.writeVInt(7) # duo victories

        self.writeVInt(9) 
        self.writeVInt(8) # highest level robo rumble

        self.writeVInt(12) 
        self.writeVInt(9) # highest level boss fight

        self.writeVInt(13)
        self.writeVInt(10) # highest power league points

        self.writeVInt(14)
        self.writeVInt(11) # some power league stuff

        self.writeVInt(15)
        self.writeVInt(12) # most challenge win
        
        playerDisplayData = PlayerDisplayData()
        playerDisplayData.setPlayer(player)
        playerDisplayData.encode(self)

        self.writeBoolean(player.AllianceID[1]!=0)
        if player.AllianceID[1]!=0:
            self.writeLong(0,1) #alliance ID
            self.writeString("haccers") #alliance name
            self.writeDataReference(8,1) # alliance icon
            self.writeVInt(1) # type
            self.writeVInt(1) # member count
            self.writeVInt(10000) # total trophies
            self.writeVInt(1) # minimum trophies to enter
            self.writeDataReference(0)
            self.writeString("CA") #location
            self.writeVInt(4) # unknown
            self.writeBoolean(True) #is Family friendly
        self.writeDataReference(25, 1) #alliance role

    def decode(self):
        return self

    def execute(message, calling_instance):
        pass

    def getMessageType(self):
        return 24113

    def getMessageVersion(self):
        return self.messageVersion
    
    def setTargetID(self, targetID):
        self.targetID = targetID