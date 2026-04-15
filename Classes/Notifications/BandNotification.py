from Classes.Notifications.BaseNotification import BaseNotification
from Classes.Entries.PlayerDisplayData import PlayerDisplayData

class BandNotification(BaseNotification):
    def __init__(self):
        super().__init__(self)
        self.player = None
        
    def encode(self, byteStream):
        super().encode(byteStream)
        playerDisplayData = PlayerDisplayData()
        playerDisplayData.setPlayer(self.player)
        playerDisplayData.encode(self)
        
    def decode(calling_instance, byteStream):
        super().decode(calling_instance, byteStream)
        return calling_instance
    
    def getAmount(self):
        return 0
    
    def getFileEntry(self):
        return 0
    
    def getNotificationType(self):
        return 82
    
    def setPlayer(self, player):
        self.player = player