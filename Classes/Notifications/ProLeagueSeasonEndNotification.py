from Classes.Notifications.BaseNotification import BaseNotification

class ProLeagueSeasonEndNotification(BaseNotification):
    def __init__(self):
        super().__init__(self)
        self.points = 0
        self.reward = 0
        self.rank = 0
        self.rankReward = 0
        
    def encode(self, byteStream):
        super().encode(byteStream)
        byteStream.writeVInt(1) # unused data!!! yesss
        byteStream.writeVInt(self.points) # my points
        byteStream.writeVInt(self.reward) # reward in star points
        byteStream.writeVInt(self.rank) # my rank
        byteStream.writeVInt(self.rankReward) # my reward in star points

    def decode(calling_instance, byteStream):
        super().decode(calling_instance, byteStream)
        byteStream.readVInt() # unused data!!! yesss
        calling_instance.points = byteStream.readVInt() # my points
        calling_instance.reward = byteStream.readVInt() # reward in star points
        calling_instance.rank = byteStream.readVInt() # my rank
        calling_instance.rankReward = byteStream.readVInt() # my reward in star points
        return calling_instance
    
    def getAmount(self):
        return 0
    
    def getFileEntry(self):
        return 0
    
    def getNotificationType(self):
        return 77