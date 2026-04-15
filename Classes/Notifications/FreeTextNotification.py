from Classes.Notifications.BaseNotification import BaseNotification

class FreeTextNotification(BaseNotification):
    def __init__(self):
        super().__init__(self)
        
    def encode(self, byteStream):
        super().encode(byteStream)
        self.writeVInt(1) # unused
        
    def decode(calling_instance, byteStream):
        super().decode(calling_instance, byteStream)
        byteStream.readVInt() # unused
        return calling_instance
    
    def getAmount(self):
        return 0
    
    def getFileEntry(self):
        return 0
    
    def getNotificationType(self):
        return 81