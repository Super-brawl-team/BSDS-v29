from Classes.Packets.PiranhaMessage import PiranhaMessage
from Classes.Entries.PlayerDisplayData import PlayerDisplayData

class LeaderboardMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0
        self.type = 0
        self.season = 0
        self.isLocal = False
        self.target = []
        self.entries = []

    def encode(self, calling_instance):
        playerIndex = 0
        self.writeVInt(self.type)
        self.writeVInt(self.season) # season?
        self.writeDataReference(*self.target)
        self.writeString("CAT" if self.isLocal else None)
        self.writeVInt(len(self.entries))
        index = 0
        for entryData in self.entries:
            if self.type != 2:      
                entryData.OwnedBrawlers = {int(k): v for k, v in entryData.OwnedBrawlers.items()}
                if entryData.ID[1] == calling_instance.player.ID[1]:
                    playerIndex = index
            else:
                if entryData.ID[1] == calling_instance.player.AllianceID[1]:
                    playerIndex = index
            self.writeVLong(0, entryData.ID[1])
            self.writeVInt(1) # wut is that
            self.writeVInt(entryData.LegendaryTrophies if self.type == 3 else entryData.OwnedBrawlers[self.target[1]]["Trophies"] if self.type == 0 else entryData.Trophies)
            self.writeBoolean(self.type!=2)
            if self.type!=2:
                self.writeString("Mr. Whatsit? Gang")
                playerDisplayData = PlayerDisplayData()
                playerDisplayData.setPlayer(entryData)
                playerDisplayData.encode(self)
            self.writeBoolean(self.type==2)
            if self.type == 2:
                self.writeString(entryData.Name)
                self.writeVInt(len(entryData.Members))
                self.writeDataReference(8, entryData.Thumbnail)
            index+=1
        self.writeVInt(0)
        self.writeVInt(playerIndex)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeString("CAT")
        

    def decode(self):
        return self

    def execute(message, calling_instance):
        pass

    def getMessageType(self):
        return 24403

    def getMessageVersion(self):
        return self.messageVersion
    
    def setType(self, type):
        self.type = type
        
    def setIsLocal(self, isLocal):
        self.isLocal = isLocal
        
    def setTarget(self, target):
        self.target = target
        
    def setSeason(self, season):
        self.season = season
        
    def setEntries(self, entries):
        self.entries = entries