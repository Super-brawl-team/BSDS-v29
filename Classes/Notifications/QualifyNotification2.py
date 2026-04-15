from Classes.Notifications.BaseNotification import BaseNotification

class QualifyNotification2(BaseNotification):
    """This notification is unused in the game but its still here fuck you supercell"""
    def __init__(self):
        super().__init__(self)
        self.result48 = 0
        
    def encode(self, byteStream):
        super().encode(byteStream)
        byteStream.writeVInt(self.result48)
        byteStream.writeVInt(0)  # what the hell its not even in ctor
        
    def decode(calling_instance, byteStream):
        super().decode(calling_instance, byteStream)
        calling_instance.result48 = byteStream.readVInt()
        byteStream.readVInt()  # what the hell its not even in ctor
        return calling_instance
    
    def getAmount(self):
        return 0
    
    def getFileEntry(self):
        return 0
    
    def getNotificationType(self):
        return 75