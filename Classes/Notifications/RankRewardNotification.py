from Classes.Notifications.BaseNotification import BaseNotification

class RankRewardNotification(BaseNotification):
    def __init__(self):
        super().__init__(self)
        self.starPointsReward = 0
        self.tokensReward = 0
        
    def encode(self, byteStream):
        super().encode(byteStream)
        byteStream.writeVInt(self.starPointsReward) # star point reward
        byteStream.writeVInt(self.tokensReward) # tokens reward

    def decode(calling_instance, byteStream):
        super().decode(calling_instance, byteStream)
        calling_instance.starPointsReward = byteStream.readVInt() # star point reward
        calling_instance.tokensReward = byteStream.readVInt() # tokens reward
        return calling_instance
    
    def getAmount(self):
        return 0
    
    def getFileEntry(self):
        return 0
    
    def getNotificationType(self):
        return 77