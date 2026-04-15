from Classes.Notifications.BaseNotification import BaseNotification
from Classes.Entries.ScoreEntry import ScoreEntry

class StarPointsNotification(BaseNotification):
    def __init__(self):
        super().__init__(self)
        self.brawlers = [] # list of ScoreEntry
        
    def encode(self, byteStream):
        super().encode(byteStream)
        byteStream.writeVInt(len(self.brawlers))
        for x in self.brawlers:
            x.encode(byteStream)
        
    def decode(calling_instance, byteStream):
        super().decode(calling_instance, byteStream)
        for x in range(byteStream.readVInt()):
            scoreEntry = ScoreEntry()
            scoreEntry.decode(byteStream)
            calling_instance.brawlers.append(scoreEntry)
        return calling_instance
    
    def getAmount(self):
        return 0
    
    def getFileEntry(self):
        return 0
    
    def getNotificationType(self):
        return 79