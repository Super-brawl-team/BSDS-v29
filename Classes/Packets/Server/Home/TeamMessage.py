from Classes.Packets.PiranhaMessage import PiranhaMessage


class TeamMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields, player):
        self.writeVInt(1) # roomTypes
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
            self.writeLong(0,1)  # playerID
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
            self.writeString(player.Name)  # player name
            self.writeVInt(0)  # player level
            self.writeVInt(28000000)  # profile icon
            self.writeVInt(43000000) # Unknown
            self.writeVInt(0) # Unknown
            self.writeDataReference(23, player.TeamGadget) # gadget
            print(player.TeamGadget)
            self.writeDataReference(23, player.TeamStarPower) # star power
            print(player.TeamStarPower)
            self.writeVInt(0) # idk
        self.writeVInt(0) # new array its timeeeee
        self.writeVInt(0) # new array its timeeeee
        self.writeVInt(0) # banned players array
        self.writeBoolean(False) # is club war
        self.writeBoolean(True) # chat enabled
        self.writeBoolean(True) # gadgets enabled

    def decode(self):
        fields = {}
        fields["PlayerCount"] = self.readVInt()
        fields["Text"] = self.readString()
        fields["Unk1"] = self.readVInt()
        super().decode(fields)
        return {}

    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 24124

    def getMessageVersion(self):
        return self.messageVersion