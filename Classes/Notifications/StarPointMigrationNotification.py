from Classes.Notifications.BaseNotification import BaseNotification

class StarPointMigrationNotification(BaseNotification):
    def __init__(self):
        super().__init__(self)
        self.gainedStarPoints = 0
        
    def encode(self, byteStream):
        super().encode(byteStream)
        byteStream.writeVInt(self.gainedStarPoints)
        
    def decode(calling_instance, byteStream):
        super().decode(calling_instance, byteStream)
        calling_instance.gainedStarPoints = byteStream.readVInt()
        return calling_instance
    
    def getAmount(self):
        return 0
    
    def getFileEntry(self):
        return 0
    
    def getNotificationType(self):
        return 80