from Classes.Debugger import Debugger

class BaseNotification:
    def __init__(self):
        self.message = ""
        self.index = 0
        self.seen = False
        self.timer = 0
        
    def encode(self, byteStream):
        byteStream.writeInt(self.index)
        byteStream.writeBoolean(self.seen)
        byteStream.writeInt(self.timer)
        byteStream.writeString(self.message)
        
    def decode(calling_instance, byteStream):
        calling_instance.index = byteStream.readInt()
        calling_instance.seen = byteStream.readBoolean()
        calling_instance.timer = byteStream.readInt()
        calling_instance.message = byteStream.readString()
        return calling_instance
    
    def getAmount(self):
        return 0
    
    def getFileEntry(self):
        return 0
    
    def getNotificationType(self):
        Debugger.error("getNotificationType needs to be overloaded")
        return -1
    
    def setMessage(self, message):
        self.message = message
    
    def setSeen(self, seen):
        self.seen = seen
        
    def setTimer(self, timer):
        self.timer = timer
        
    def setIndex(self, index):
        self.index = index