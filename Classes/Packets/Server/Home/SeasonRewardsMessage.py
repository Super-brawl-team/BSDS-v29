from Classes.Packets.PiranhaMessage import PiranhaMessage


class SeasonRewardsMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0
        self.type = 0

    def encode(self, calling_instance):
        self.writeVInt(self.type) # type
        if self.type == 5:
            rewardStart = [1,2,3,4,5,6,7,8,9]
            rewardEnd = [1,2,3,4,5,6,7,8,9]
            rewardAmount = [10,10,100,10,10,100,10,10,300]
            rewardExtraData = [525, 550, 600, 650, 700, 725, 750, 775, 800, 825, 850, 875, 900, 925, 950, 975, 1000, 1025]
            rewardTypes = [1,1,0,1,1,0,1,1,0]
        else:
            rewardStart = [550, 600, 650, 700, 750, 800, 850, 900, 950, 1000, 1050, 1100, 1150, 1200, 1250, 1300, 1350, 1400]
            rewardEnd = [599, 649, 699, 749, 799, 849, 899, 949, 999, 1049, 1099, 1149, 1199, 1249, 1299, 1349, 1399, -1]
            rewardAmount = [70, 120, 160, 200, 220, 240, 260, 280, 300, 320, 340, 360, 380, 400, 420, 440, 460, 480]
            rewardExtraData = [525, 550, 600, 650, 700, 725, 750, 775, 800, 825, 850, 875, 900, 925, 950, 975, 1000, 1025]
            rewardTypes = [0]*19
        self.writeVInt(len(rewardStart))
        for x in range(len(rewardStart)):
            self.writeVInt(rewardStart[x])
            self.writeVInt(rewardEnd[x])
            self.writeVInt(rewardAmount[x])
            self.writeVInt(rewardExtraData[x])
            self.writeVInt(rewardTypes[x])
            self.writeBoolean(True) # Unk bool
        self.writeBoolean(True)
        if True:
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeDataReference(16, 8)
            self.writeVInt(0)
        

    def decode(self):
        self.type = self.readVInt()
        return self

    def execute(message, calling_instance):
        pass

    def getMessageType(self):
        return 24123

    def getMessageVersion(self):
        return self.messageVersion
    
    def setType(self, type):
        self.type = type