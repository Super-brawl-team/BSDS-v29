from Classes.Commands.LogicServerCommand import LogicServerCommand

class LogicDiamondsAddedCommand(LogicServerCommand):
    def __init__(self, commandData):
        super().__init__(commandData)
        self.isActionFromDebug = False
        self.addedDiamonds = 0

    def encode(self, player):
        self.writeBoolean(self.isActionFromDebug); # i suppose isActionFromDebug
        self.writeInt(self.addedDiamonds); # lazy
        self.writeInt(0); # what is this lmao
        self.writeInt(0); # bruh :skull:
        self.writeString("uwu"); # transaction id if its asked from inapppurchases
        self.writeVInt(0); # duh
        LogicServerCommand.encode(self)
        return self.messagePayload

    def decode(self, calling_instance):
        self.isActionFromDebug = calling_instance.readBoolean()
        self.addedDiamonds = calling_instance.readInt() 
        calling_instance.readInt()
        calling_instance.readInt()
        calling_instance.readString()
        calling_instance.readVInt()
        return LogicServerCommand.decode(calling_instance)

    def getCommandType(self):
        return 202
    
    def setIsActionFromDebug(self, isActionFromDebug):
        self.isActionFromDebug = isActionFromDebug
        
    def setAddedDiamonds(self, addedDiamonds):
        self.addedDiamonds = addedDiamonds
    