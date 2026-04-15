from Classes.Notifications.BaseNotification import BaseNotification

class QualifyNotification(BaseNotification):
    def __init__(self):
        super().__init__(self)
        
    def encode(self, byteStream):
        super().encode(byteStream)
        
    def decode(calling_instance, byteStream):
        super().decode(calling_instance, byteStream)
        return calling_instance
    
    def getAmount(self):
        return 0
    
    def getFileEntry(self):
        return 0
    
    def getNotificationType(self):
        return 76