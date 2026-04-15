from Classes.Commands.LogicCommand import LogicCommand
from Classes.Messaging import Messaging

class LogicSetPlayerThumbnailCommand(LogicCommand):
    def __init__(self, commandData):
        super().__init__(commandData)
        self.targetThumbnail = 0

    def encode(self):
        LogicCommand.encode(self)
        self.writeDataReference(self.targetThumbnail)
        return self.messagePayload

    def decode(self, calling_instance):
        LogicCommand.decode(calling_instance)
        self.targetThumbnail = calling_instance.readDataReference()
        return self

    def execute(self, calling_instance, cryptoInit):
        calling_instance.player.Thumbnail = self.targetThumbnail[1]
        calling_instance.db.replaceValue("Thumbnail", self.targetThumbnail[1], calling_instance.player)

    def getCommandType(self):
        return 505