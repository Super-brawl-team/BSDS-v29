from Classes.Commands.LogicServerCommand import LogicServerCommand
from Classes.Entries.DeliveryUnit import DeliveryUnit

class LogicGiveDeliveryItemsCommand(LogicServerCommand):
    def __init__(self, commandData):
        super().__init__(commandData)
        self.deliveryUnits = []
        self.milestoneType = 0
        self.milestoneTrack = 0
        self.season = 0

    def encode(self, player):
        self.writeVInt(0) # I dont even know
        self.writeVInt(len(self.deliveryUnits))
        for deliveryUnit in self.deliveryUnits:
            deliveryUnit.encode(self)
        self.writeBoolean(False) # forced drops
        if False:
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            for x in range(0):
                self.writeVInt(0)
        self.writeVInt(self.milestoneType) # milestoneType
        self.writeVInt(self.milestoneTrack) # milestoneTrack
        self.writeVInt(self.season) # bralpass season
        LogicServerCommand.encode(self)
        return self.messagePayload

    def decode(self, calling_instance):
        calling_instance.readVInt()
        for x in range(calling_instance.readVInt()):
            deliveryUnit = DeliveryUnit()
            deliveryUnit.decode(calling_instance)
            calling_instance.deliveryUnits.append(deliveryUnit)
        if calling_instance.readBoolean():
            calling_instance.readVInt()
            calling_instance.readVInt()
            for x in range(calling_instance.readVInt()):
                calling_instance.readVInt()
        self.milestoneType = calling_instance.readVInt()
        self.milestoneTrack = calling_instance.readVInt()
        self.season = calling_instance.readVInt()
        return LogicServerCommand.decode(calling_instance)

    def getCommandType(self):
        return 203
    
    def setDeliveryUnits(self, deliveryUnits):
        self.deliveryUnits = deliveryUnits
        
    def setMilestoneType(self, milestoneType):
        self.milestoneType = milestoneType
        
    def setMilestoneTrack(self, milestoneTrack):
        self.milestoneTrack = milestoneTrack
        
    def setSeason(self, season):
        self.season = season