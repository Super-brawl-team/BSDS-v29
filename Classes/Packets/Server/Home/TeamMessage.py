from Classes.Packets.PiranhaMessage import PiranhaMessage
from Classes.Entries.PlayerDisplayData import PlayerDisplayData

class TeamMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, calling_instance):
        player = calling_instance.player
        self.writeVInt(1) # roomType
        self.writeBoolean(True) # practice
        self.writeVInt(3) # capacity / maxmembers
        self.writeLong(0,1) # roomID
        self.writeVInt(0)
        self.writeBoolean(False) # broadcast to friends
        self.writeBoolean(False) # broadcast to band
        self.writeVInt(0)
        self.writeVInt(0) # location index
        self.writeDataReference(15,player.SelectedMap) # locationID

        self.writeVInt(1)
        for member in range(1):
            self.writeBoolean(True)  # owner
            self.writeLong(0,5)  # playerID
            self.writeDataReference(16, player.SelectedBrawler)  # characterid
            self.writeDataReference(29, player.SelectedSkins.get(player.SelectedBrawler, 0))  # skinid
            self.writeVInt(0) # character trophies
            self.writeVInt(0) # character high trophies
            self.writeVInt(10) # character power level
            self.writeVInt(3) # status
            self.writeBoolean(False) # ready status
            self.writeVInt(0) # team
            self.writeVInt(0) # idk
            self.writeVInt(0)  # isk
            playerDisplayData = PlayerDisplayData()
            playerDisplayData.setPlayer(player)
            playerDisplayData.encode(self)
            self.writeDataReference(23, player.TeamStarPower) # gadget
            self.writeDataReference(23, player.TeamGadget) # star power
            self.writeVInt(0) # idk
        self.writeVInt(0) # new array its timeeeee
        self.writeVInt(0) # new array its timeeeee
        self.writeBoolean(False) # is club war
        self.writeBoolean(not player.ChatMuted) # chat enabled
        self.writeBoolean(True) # gadgets enabled

    def decode(self):
        return self

    def execute(message, calling_instance):
        pass

    def getMessageType(self):
        return 24124

    def getMessageVersion(self):
        return self.messageVersion